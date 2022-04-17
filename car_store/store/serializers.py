from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from car_store.store.models import Store, Car


class CarSerializer(ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())

    class Meta:
        fields = ('id', 'title', 'available', 'store')
        model = Car


class StoreSerializer(ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'title', 'cars')
        model = Store

