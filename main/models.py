from django.db import models

class ExamForm(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=15)