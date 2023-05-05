from django.forms import model_to_dict
from rest_framework import generics
from employee.serializers import EmployeeSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from employee.models import Vote
from restaurant.models import Menu
from inforce_test_task.config import settings
from restaurant.helpers import custom_error_response


headers = {
    'Build-Version': settings.BUILD_VERSION
}


class GetEmployeeAPIView(generics.ListAPIView):
    """
    API view to get a list of all employees.

    This view returns a list of serialized employee objects in JSON format.
    The view requires authentication, so the requesting user must provide a valid access token in the request headers.

    HTTP Methods supported: GET
    """


    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        query = User.objects.all() 
        serialized_data = EmployeeSerializer(query, many=True).data

        return Response(serialized_data, headers=headers)


class RegisterAPIView(generics.CreateAPIView):
    """
    API view to register a new employee.

    This view creates a new user object in the database with the provided user data.
    The view returns a serialized user object in JSON format.

    HTTP Methods supported: POST
    """
       

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class VoteForMenuAPIView(APIView):
    """
    API view to allow an authenticated user to vote for a menu.

    This view creates a new vote object in the database and updates the vote count for the corresponding menu object.
    The view returns a serialized vote object in JSON format.

    HTTP Methods supported: GET
    """

    
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        current_user_id = request.user.id
        
        try:
            menu_id = request.query_params["id"]
        except:
            return custom_error_response(
                                         description="You should use menu ID as query parameter in request",
                                         status_code=400,
                                         headers=headers
                                         )

        current_user = User.objects.filter(id=current_user_id).first()
        menu = Menu.objects.filter(id=menu_id).first()
        if not menu or not menu_id:
            return custom_error_response(
                                         description="There is no menu with such ID",
                                         status_code=404,
                                         headers=headers
                                         )

        new_vote = Vote.objects.create(
            employee=current_user,
            menu=menu
        )

        menu.votes += 1
        menu.save()

        return Response(model_to_dict(new_vote))
