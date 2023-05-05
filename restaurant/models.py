from django.db import models


WEEKDAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]


class Restaurant(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=100)
    weekday = models.CharField(max_length=50, choices=WEEKDAY_CHOICES)
    votes = models.IntegerField(default=0)
    restaurant = models.ForeignKey(Restaurant, related_name="menus", on_delete=models.SET_NULL, null=True) 
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.weekday} - {self.votes}"
    