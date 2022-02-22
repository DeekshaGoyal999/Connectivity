from django.db import models

User=settings.AUTH_USER_MODEL

# Create your models here.



class Tweet(models.Model):
    #id= models.AutoField(primary_key=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
