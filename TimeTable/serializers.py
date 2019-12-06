from rest_framework import serializers
from .models import *
from django.contrib.auth.models import *

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username')
		
class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'

class EventAllSerializer(serializers.ModelSerializer):
	category = CategorySerializer()
	class Meta:
		model = Event
		fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
	category = CategorySerializer()
	class Meta:
		model = Event
		fields = ('events_name', 'info', 'img', 'category')

class OrderSerializer(serializers.ModelSerializer):
	order_user = UserSerializer()
	event = EventSerializer()
	class Meta:
		model = Order
		fields = '__all__'
