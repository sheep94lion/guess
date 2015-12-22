from django.db import models

# Create your models here.
class GuessSubject(models.Model):
	content = models.CharField(max_length = 400)
	choiceA = models.CharField(max_length = 100)
	choiceB = models.CharField(max_length = 100)
	stepsA = models.IntegerField()
	stepsB = models.IntegerField()