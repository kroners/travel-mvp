from rest_framework.views import APIView
from .serializers import prueba_POST_Serializer
from .models import prueba_POST
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse, Http404

# Create your views here.
class prueba_POST_APIView(APIView): 
    serializer_class= prueba_POST_Serializer
    model = serializer_class.Meta.model
    def get(self,request,format=None):
        prueba= prueba_POST.objects.all()
        serializer= prueba_POST_Serializer(prueba)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = prueba_POST_Serializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


       