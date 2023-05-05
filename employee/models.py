from django.db import models
from restaurant.models import Menu
from django.contrib.auth.models import User


class Vote(models.Model):
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} - {self.menu}"

