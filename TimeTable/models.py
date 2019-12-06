from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    events_name = models.CharField(max_length=200)
    tickets_count = models.IntegerField()
    info = models.TextField()
    geolocation = models.CharField(max_length=200, default="")
    img = models.ImageField(upload_to='img')
    date = models.DateField('date published')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    def __unicode__(self):
    	return self.category_name
    def __str__(self):
        return 'id: {} name: {}'.format(self.id, self.events_name)


class Category(models.Model):
    img = models.ImageField(upload_to='category')
    category_name = models.CharField(max_length=200)
    def __unicode__(self):
    	return self.category_name
    def __str__(self):
        return 'id: {} name: {}'.format(self.id, self.category_name)

class Order(models.Model):
	event = models.ForeignKey('Event', on_delete=models.CASCADE, default=1)
	order_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	tickets_count = models.IntegerField()
	price = models.IntegerField()
	def __str__(self):
		return 'id: {} name: {}'.format(self.id, self.order_user)