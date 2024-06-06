from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User


# Create your models here.
# # Custom User Manager
# class UserManager(BaseUserManager):
#     def create_user(self, username, password=None):
#         if not username:
#             raise ValueError("Users must have a username")
#         user = self.model(username=username)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password):
#         user = self.create_user(
#             username=username,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

# # User Model
# class User(AbstractBaseUser):
#     username = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)

#     objects = UserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []  # Passwords are required by default

#     def __str__(self):
#         return self.username

# Trip Model
class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_name = models.CharField(max_length=255)
    #location = models.CharField(max_length=255)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    #transportation = models.CharField(max_length=255)

    def __str__(self):
        return self.trip_name

# Place Model
class Place(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=255)

    def __str__(self):
        return self.place_name
    
class Plan(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()

    def __str__(self):
        return self.place.place_name
    