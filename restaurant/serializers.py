from rest_framework import serializers
from restaurant.models import Restaurant, Menu


class RestaurantSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Restaurant
        fields = ('id', 'title', 'menus', 'created_at', 'updated_at')
        read_only_fields = ['menus']
        

class MenuSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Menu
        fields = ('id', 'title', 'weekday', 'votes', 'restaurant', 'created_at', 'updated_at')
        read_only_fields = ['votes']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['restaurant'] = instance.restaurant.title
        return data
