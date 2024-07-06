from django.urls import path
from .views import HomeView, DiscountListAPIView, AirConditionerListAPIView, MobilePhonesListAPIView, HouseholdAppliancesSerializerListAPIView,\
    BooksListAPIView, TVListAPIView, LaptopsListAPIView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('discount/', DiscountListAPIView.as_view(), name='discount'),
    path('airconditioner/', AirConditionerListAPIView.as_view(), name='airconditioner'),
    path('mobilephone/', MobilePhonesListAPIView.as_view(), name='mobilephone'),
    path('householdappliances/', HouseholdAppliancesSerializerListAPIView.as_view(), name='householdappliances'),
    path('books/', BooksListAPIView.as_view(), name='books'),
    path('tv/', TVListAPIView.as_view(), name='tv'),
    path('laptop/', LaptopsListAPIView.as_view(), name='laptop'),
]