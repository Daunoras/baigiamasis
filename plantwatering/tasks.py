from datetime import date
from celery import shared_task
from django.core.mail import send_mail
from .models import Plant
from mysite.settings import EMAIL_HOST_USER

@shared_task
def send_watering_notifications():
    needs_watering = Plant.objects.filter(next_watering__lte=date.today())
    for plant in needs_watering:
        if plant.owner.email:
            recipient = plant.owner.email
        else:
            continue
        if plant.name:
            message = f"{plant.name} needs watering. http://127.0.0.1:8000/plants/myplants/{plant.pk}"
        elif plant.sciname:
            message = \
                f"Your plant {plant.sciname} needs watering. http://127.0.0.1:8000/plants/myplants/{plant.pk}"
        else:
            message = \
                f"One of your plants needs to be watered. http://127.0.0.1:8000/plants/myplants/{plant.pk}"
        send_mail(
            "Time to water your plant", message, EMAIL_HOST_USER,
            [recipient],
            fail_silently=False,
        )
