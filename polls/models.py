from django.db import models

# Create your models here.
class Question(models.Model):
    content = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.content

class Answer(models.Model):
    content = models.CharField(max_length=200)
    image   = models.CharField(max_length=200)

    def __str__(self):
        return self.content

