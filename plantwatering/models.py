from datetime import timedelta, date
from django.db import models
from django.contrib.auth.models import User

class Plant(models.Model):
    sciname = models.CharField('Scientific name', max_length=300, null=True, blank=True)
    watering = models.CharField('Watering', max_length=30, null=True, blank=True)
    name = models.CharField('Name', max_length=100, null=True, blank=True)
    pic = models.ImageField('Picture', upload_to='pics', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    watered = models.DateField('Last watered', null=True, blank=True)
    next_watering = models.DateField('Next watering', null=True, blank=True)

    def __str__(self):
        representation = ''
        if self.name:
            representation = self.name
        if self.sciname:
            if representation.__len__() > 0:
                representation += ' '
            representation += self.sciname
        if representation == '':
            representation = f"Unnamed plant"
        return representation

    def min_time(self):
        if self.watering.find('-') != -1:
            days = int(self.watering.split('-')[0])
        else:
            days = int(self.watering.split(' ')[0])
        return days

    def max_time(self):
        days = int(self.watering.split('-')[-1].split()[0])
        return days

    def save(self, *args, **kwargs):
        if not self.watered:
            self.watered = date.today()
        if self.watering:
            self.next_watering = self.watered + timedelta(days=self.min_time())
        super(Plant, self).save(*args, **kwargs)


    @property
    def needs_watering(self):
        needs = False
        if self.watered and self.watering:
            if (self.watered + timedelta(days=self.min_time())) < date.today() and (self.watered + timedelta(days=self.max_time())) > date.today():
                needs = True
        return needs

    @property
    def drying(self):
        dry = False
        if self.watered and self.watering:
            if (self.watered + timedelta(days=self.max_time())) < date.today():
                dry = True
        return dry

    def water(self):
        self.watered = date.today()
        self.save()