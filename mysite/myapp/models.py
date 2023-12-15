from django.db import models


class Repetitor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.CharField(max_length=200)
    photo = models.ImageField(blank=True, upload_to='images')
    education = models.CharField(max_length=200)
    experience = models.IntegerField()

    def __str__(self):
        return self.name