from django.db import models


class Repetitor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.CharField(max_length=200)
    photo = models.ImageField(blank=True, upload_to='images')
    education = models.CharField(max_length=200)
    experience = models.IntegerField()
    specialty = models.CharField(blank=True, max_length=100)
    cost = models.IntegerField(blank=True)

    def __str__(self):
        return self.name