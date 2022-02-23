from django.db import models
from django.conf import settings


User=settings.AUTH_USER_MODEL

# # Create your models here.


class Post(models.Model):
    # id= models.AutoField(primary_key=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-id']