from django.urls import path
from .views import select_plant, create_plant
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select/', select_plant, name='select'),
    path('create/', create_plant, name='create'),
    path('myplants', views.OwnedPlantsListView.as_view(), name='my-plants'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('myplants/<int:pk>', views.PlantDetailView.as_view(), name='plant-details'),
    path('myplants/custom', views.CustomPlantCreateView.as_view(), name='custom-plant'),
    path('myplants/<int:pk>/update', views.PlantUpdateView.as_view(), name='plant-update'),
    path('myplants/<int:pk>/delete', views.PlantDeleteView.as_view(), name='plant-delete'),

]