from django.db import models

class Person(models.Model):
	first_name = models.CharField(max_length=30)
	lsat_name = models.CharField(max_length=30)
