from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.views.generic import ListView
from .models import Discounts, AirConditioner, MobilePhones, HouseholdAppliances,\
    Books, TV, Laptops
from .serializers import DiscountsSerializer, AirConditionerSerializer, MobilePhonesSerializer,\
    HouseholdAppliancesSerializer, BooksSerializer, TVSerializer, LaptopsSerializer

# Create your views here.

class HomeView(ListView):
    model  = Books
    template_name = 'books/index.html'

class DiscountListAPIView(ListAPIView):
    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer

class AirConditionerListAPIView(ListAPIView):
    queryset = AirConditioner.objects.all()
    serializer_class = AirConditionerSerializer

class MobilePhonesListAPIView(ListAPIView):
    queryset = MobilePhones.objects.all()
    serializer_class = MobilePhonesSerializer

class HouseholdAppliancesSerializerListAPIView(ListAPIView):
    queryset = HouseholdAppliances.objects.all()
    serializer_class = HouseholdAppliancesSerializer

class BooksListAPIView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class TVListAPIView(ListAPIView):
    queryset = TV.objects.all()
    serializer_class = TVSerializer

class LaptopsListAPIView(ListAPIView):
    queryset = Laptops.objects.all()
    serializer_class = LaptopsSerializer

