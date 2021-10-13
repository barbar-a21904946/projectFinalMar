from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    title= models.CharField(max_length=255)
    summary=models.CharField(max_length=255)
    content= models.TextField()
    author=models.ForeignKey(User,on_delete=models.PROTECT)
    created_at=models.DateField(auto_now=True)


def self(args):
    return self.title



