import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from .managers import UserManager

def get_id():
    x = uuid.uuid4().hex[:6].upper()
    return x
class Machine(models.Model):
    machine_code = models.CharField(max_length=50,primary_key=True,unique=True,default='')
    description = models.CharField(max_length=100,unique=False,default='')
    hourly_rent = models.FloatField(null=True,blank=True,default=None)
    maxhoursperday = models.IntegerField(default=0)

    class Meta:
        ordering = ['machine_code']

    def __str__(self):
        return self.machine_code

    def save(self, *args, **kwargs):
        if not self.machine_code:
            self.machine_code = get_id()

        super().save(*args,**kwargs)



class Job(models.Model):
    code = models.CharField(max_length=50,primary_key=True,unique=True,default='')
    description = models.CharField(max_length=100,default='')
    hourly_rate = models.FloatField(null=True,blank=True,default=None)
    maxhoursperday = models.IntegerField(default=0)

    def save(self,*args,**kwargs):
        if not self.code:
            self.code = get_id()
        super().save(*args,**kwargs)


    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code


class Timecard(models.Model):
    sitecode = models.CharField(max_length=50,primary_key=True,unique=True,default='')
    contractor_name = models.CharField(max_length=75,default='')
    total_hours = models.IntegerField(default=0)
    total_amount = models.FloatField(null=True,blank=True,default=None)
    status = "review"

    def save(self,*args,**kwargs):
        if not self.sitecode:
            self.sitecode = get_id()
        super().save(*args,**kwargs)


    class Meta:
        ordering = ['sitecode']

    def __str__(self):
        return self.sitecode


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40,unique=True,default='')
    name = models.CharField(max_length=40,unique=False,default='')
    is_admin = models.BooleanField(_('admin status'),default=False)
    password = models.CharField(max_length=100,editable=False,default='')
    listofjobs = models.ManyToManyField(Job,on_delete=models.DO_NOTHING,null=True)
    listofmachines = models.ManyToManyField(Machine,on_delete=models.DO_NOTHING,null=True)
    listoftimecards = models.ManyToManyField(Timecard,on_delete=models.DO_NOTHING,null=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','password','is_admin']

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return self.is_admin



