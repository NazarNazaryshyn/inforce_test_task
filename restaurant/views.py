from rest_framework.response import Response
from rest_framework import generics
from restaurant.models import Restaurant, Menu
from django.forms import model_to_dict
from restaurant.serializers import RestaurantSerializer, MenuSerializer
from rest_framework.permissions import IsAuthenticated
import calendar
import datetime
from inforce_test_task.config import settings
from restaurant.helpers import custom_error_response


headers = {
    'Build-Version': settings.BUILD_VERSION
}


class ResturantAPIView(generics.ListCreateAPIView):
    """
    API view to get a list of all restaurants and to create a new one.

    This view returns a list of serialized restaurants objects in JSON format.
    The view requires authentication, so the requesting user must provide a valid access token in the request headers.

    HTTP Methods supported: GET, POST
    """


    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        query = Restaurant.objects.all()
        serialized_data = RestaurantSerializer(query, many=True).data

        return Response(serialized_data, headers=headers)


class MenuAPIView(generics.ListCreateAPIView):
    """
    API view to get a list of all menu and to create a new one.

    This view returns a list of serialized menu objects in JSON format.
    The view requires authentication, so the requesting user must provide a valid access token in the request headers.

    HTTP Methods supported: GET, POST
    """


    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        query = Menu.objects.all()
        serialized_data = MenuSerializer(query, many=True).data

        return Response(serialized_data, headers=headers)

    def post(self, request, *args, **kwargs):
        try:
            if not request.data['restaurant']:
                return custom_error_response(
                                            description="You should provide restaurant in order to create menu instance",
                                            status_code=400,
                                            headers=headers
                                            )
            elif request.data['weekday'] not in calendar.day_name:
                return custom_error_response(
                                             description="Please provide correct weekday e.g Monday, Tuesday etc.",
                                             status_code=404,
                                             headers=headers
                                            )
            
            restaurant = Restaurant.objects.filter(id=request.data['restaurant']).first()
            if not restaurant:
                return custom_error_response(
                                             description="The restaurant you provided does not exist",
                                             status_code=404,
                                             headers=headers
                                             )
    
            new_menu = Menu.objects.create(
                title=request.data['title'],
                weekday=request.data['weekday'],
                restaurant=restaurant
            )

            return Response(model_to_dict(new_menu), headers=headers)
        except Exception:
            return custom_error_response(
                                         description="You should provide title, weekday and restaurant ID",
                                         status_code=400,
                                         headers=headers
                                         )
        

class GetCurrentDayMenusAPIView(generics.ListAPIView):
    """
    API view to get a list of all current day menus sorted in relation to votes number .

    This view returns a list of serialized menu objects in JSON format.
    The view requires authentication, so the requesting user must provide a valid access token in the request headers.

    HTTP Methods supported: GET
    """
      

    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        today = datetime.datetime.today()
        weekday_name = today.strftime('%A')

        query = Menu.objects.filter(weekday=weekday_name).order_by('-votes').all()
        serialized_data = MenuSerializer(query, many=True).data

        return Response(serialized_data, headers=headers)
