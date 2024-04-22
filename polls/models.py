from django.db import models
from uuid import uuid4
import os

def get_upload_path(instance,filename):
    return os.path.join("images",str(instance.pk),filename) 

# Create your models here.
class Question(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    content = models.CharField(max_length=1024,blank=True,null=True)
    image = models.ImageField(upload_to=get_upload_path,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return str(self.content)

class Answer(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    content = models.CharField(max_length=1024)
    image = models.ImageField(upload_to=get_upload_path,blank=True,null=True)

    def __str__(self):
        return str(self.content)

