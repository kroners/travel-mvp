from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from programs import views

urlpatterns = [
    path('programs/', views.ProgramList.as_view()),
    path('programs/<int:pk>/', views.ProgramDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)