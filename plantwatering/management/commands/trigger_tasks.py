from django.core.management.base import BaseCommand
from plantwatering.tasks import send_watering_notifications

class Command(BaseCommand):
    help = 'Trigger Celery tasks manually'

    def handle(self, *args, **options):
        result = send_watering_notifications.delay()
        self.stdout.write(self.style.SUCCESS(f"task triggered: {result.id}"))