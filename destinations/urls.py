from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from destinations import views

urlpatterns = [
    path('countries/', views.CountryList.as_view()),
    path('destinations/', views.DestinationList.as_view()),
    path('destinations/<int:pk>/', views.DestinationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)