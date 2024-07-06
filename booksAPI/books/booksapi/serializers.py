from rest_framework import serializers
from .models import Discounts, AirConditioner, MobilePhones, HouseholdAppliances,\
    Books, TV, Laptops


class DiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discounts
        fields = '__all__'


class AirConditionerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirConditioner
        fields = '__all__'

class MobilePhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePhones
        fields = '__all__'

class HouseholdAppliancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseholdAppliances
        fields = '__all__'

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class TVSerializer(serializers.ModelSerializer):
    class Meta:
        model = TV
        fields = '__all__'

class LaptopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptops
        fields = '__all__'

