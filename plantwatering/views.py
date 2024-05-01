from django.contrib import messages
from django.contrib.auth.forms import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CustomPlantCreateForm, UserUpdateForm
from .models import Plant
from .utils import fetch_api_data, plant_from_api_data, select_object_and_create


def index(request):
    # write vars and what they are equal to. Then put the vars into the context dict ex.:
    # var = smth * sum(x)
    # {'var': var}
    context = {}
    return render(request, 'index.html',context=context)

@login_required
def select_plant(request):
    if request.method == 'GET':
        return render(request, 'input_text.html')
    elif request.method == 'POST':
        input_text = request.POST.get('input_text')
        if input_text:
            input_text = input_text.replace(" ", "_")
            part = f"-list?key=sk-4ZiR66169c759a2575057&q={input_text}"
            data = fetch_api_data(part)['data']

            if data:
                return render(request, 'select_object.html', {'api_data': data})
            else:
                return HttpResponse("Failed to fetch data from API.")
        else:
            return HttpResponse("Please provide input text.")

@login_required
def create_plant(request):
    if request.method == 'POST':
        id = request.POST.get('selected_object')
        if id:
            part = f"/details/{id}?key=sk-4ZiR66169c759a2575057"
            selected_data = fetch_api_data(part)
            if selected_data:
                plant_from_api_data(selected_data, request.user)

                return redirect('my-plants')
            else:
                return HttpResponse("Failed to fetch selected object data from API.")
        else:
            return HttpResponse("Please select an object.")
    else:
        return redirect('select')


class OwnedPlantsListView(LoginRequiredMixin, generic.ListView):
    model = Plant
    template_name = 'my_plants.html'


    def get_queryset(self):
        return Plant.objects.filter(owner=self.request.user)

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'The email adress {email} is already taken')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'User {username} has been registered')
                    return redirect('login')
        else:
            messages.error(request, 'The passwords do not match')
            return redirect('register')
    return render(request, 'register.html')

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f"Profile updated")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'profile.html', context)

class PlantDetailView(LoginRequiredMixin, DetailView):
    model = Plant
    template_name = 'plant_details.html'

    def post(self, request, *args, **kwargs):
        plant = self.get_object()
        plant.water()
        return redirect('plant-details',  pk=plant.pk)
class CustomPlantCreateView(LoginRequiredMixin, CreateView):
    model = Plant
    # fields = ['name', 'pic', 'watered', 'watering', 'sciname']
    success_url = "/plants/myplants"
    template_name = 'custom_plant.html'
    form_class = CustomPlantCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PlantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Plant
    fields = ['name', 'pic', 'watered', 'watering', 'sciname']
    success_url = "/plants/myplants"
    template_name = 'custom_plant.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        plant = self.get_object()
        return self.request.user == plant.owner

class PlantDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Plant
    success_url = "/plants/myplants"
    template_name = 'plant_delete.html'

    def test_func(self):
        plant = self.get_object()
        return self.request.user == plant.owner
