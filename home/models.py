from django.db import models

class userModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False,default='')
    age = models.IntegerField(blank=False,default=0)
    gender = models.CharField(max_length=10,blank=False,default='')
    username = models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,unique=True,blank=False)
    phone = models.CharField(max_length=10,unique=True,blank=False)    
    class Meta:
        db_table="ttm_users"
class adminModel(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,unique=True,blank=False)
    phone = models.CharField(max_length=10,unique=True,blank=False)    
    class Meta:
        db_table="ttm_admin"