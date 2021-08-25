from django.urls import path
from prueba_POST import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('prueba_POST/', views.prueba_POST_APIView.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
