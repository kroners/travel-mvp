from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from services import views

urlpatterns = [
    path('hotel_categories/', views.HotelCategoryList.as_view()),
    path('hotel_categories/<int:pk>/', views.HotelCategoryDetail.as_view()),
    path('services/', views.HotelCategoryList.as_view()),
    path('services/<int:pk>/', views.HotelCategoryDetail.as_view()),
    path('service_types/', views.HotelCategoryList.as_view()),
    path('service_types/<int:pk>/', views.HotelCategoryDetail.as_view()),
    path('room_types/', views.HotelCategoryList.as_view()),
    path('room_types/<int:pk>/', views.HotelCategoryDetail.as_view()),
    path('food_services/', views.HotelCategoryList.as_view()),
    path('food_services/<int:pk>/', views.HotelCategoryDetail.as_view()),
    path('trip_profiles/', views.HotelCategoryList.as_view()),
    path('trip_profiles/<int:pk>/', views.HotelCategoryDetail.as_view()),
    path('activities/', views.HotelCategoryList.as_view()),
    path('activities/<int:pk>/', views.HotelCategoryDetail.as_view()),
    path('traveler_types/', views.HotelCategoryList.as_view()),
    path('traveler_types/<int:pk>/', views.HotelCategoryDetail.as_view()),
    path('languages/', views.HotelCategoryList.as_view()),
    path('languages/<int:pk>/', views.HotelCategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)