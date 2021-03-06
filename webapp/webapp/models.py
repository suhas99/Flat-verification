from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password
from phonenumber_field.modelfields import PhoneNumberField


class Meta(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(default=0)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True,blank=True,null=True)
    profile_image = models.ImageField(upload_to='image/%Y/%m/%d',blank=True,null=True)
    preferences = models.CharField(max_length=2000, blank=True,null=True)
    status = models.CharField(max_length=255, blank=True,null=True)
    tel = PhoneNumberField(blank=True,null=True)
    extra = models.CharField(max_length=1000,blank=True,null=True)
    type = models.CharField(max_length=255,blank=True,null=True)
    is_staff = models.BooleanField(default=False,blank=True,null=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)

    def __str__(self):
        return str(self.id)

class Alerts(Meta):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    detail = models.CharField(max_length=2000)
    status = models.CharField(max_length=255)
    app_redirect = models.CharField(max_length=2000)


class Projects(Meta):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=2000)
    location = models.CharField(max_length=2000)
    status = models.CharField(max_length=2000)
    type = models.CharField(max_length=2000)
    nm_meta = models.CharField(max_length=2000,blank=True)
    extra = models.CharField(max_length=2000,blank=True,null=True)

    def __str__(self):
        return str(self.id)


#
# class House(Meta):
#     # project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
#     # name = models.CharField(max_length=2000)
#     # extra = models.CharField(max_length=2000)
#     # type = models.CharField(max_length=2000)
#     # status = models.CharField(max_length=2000)
#     assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.id)


class Floors(Meta):
    house_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    type = models.CharField(max_length=2000)
    name = models.CharField(max_length=2000)
    nm_meta = models.CharField(max_length=2000,blank=True)
    extra = models.CharField(max_length=2000,blank=True)

    def __str__(self):
        return str(self.id)


class Blob(Meta):
    floor_id = models.ForeignKey(Floors, on_delete=models.CASCADE)
    data = models.FileField(upload_to='files/')
    nm_meta = models.CharField(max_length=2000,blank=True)

    def __str__(self):
        return "%s %s" % (self.floor_id, self.data)
