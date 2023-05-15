from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class TaskView(APIView):
    def get(self, requests):
        return Response({"name": "ros"}, status=status.HTTP_200_OK)
