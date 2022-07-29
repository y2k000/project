from django.db import models
from django.db.models import Model
import uuid

class UserDetails(models.Model):
    userid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    username=models.CharField(max_length=106)
    email=models.EmailField(max_length=106)
    #password=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    firstname=models.CharField(max_length=106)
    lastname=models.CharField(max_length=106)
    user_profile_picture=models.ImageField(upload_to = "images/", null=True)
