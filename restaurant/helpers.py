from rest_framework.response import Response


def custom_error_response(description, status_code, headers):
    return Response({
                    "Failure": "Error",
                    "Description": description
                    },
                    headers=headers,
                    status=status_code)
