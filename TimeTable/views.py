from django.shortcuts import *
from django.http import *
from .models import *
from django.core import *
from rest_framework.views import *
from rest_framework.response import *
from .serializers import *
import datetime

# Create your views here.
def index(request):
	list_of_category = Category.objects.all()
	today = datetime.date.today()
	day = datetime.timedelta(days = 7)
	yesterday = today + day
	list_of_events = Event.objects.filter(date__range=["" + str(today), "" + str(yesterday)])[:4]	
	context = {'list_of_events': list_of_events, 'list_of_category': list_of_category}
	return render(request, 'TimeTable/newindex.html', context)

def eventsList(request, cat):
	category = get_object_or_404(Category, pk=cat)
	catr = Category.objects.all()
	list_of_events = Event.objects.filter(category=category)[:9]
	context = {'list_of_events': list_of_events, 'list_of_category': catr}
	return render(request, 'TimeTable/eventsList.html', context)

def events(request):
	list_of_category = Category.objects.all()
	list_of_events = Event.objects.all()[:3]
	context = {'list_of_category': list_of_category, 'list_of_events': list_of_events}
	return render(request, 'TimeTable/events.html', context)
def eventDesc(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	context = {'event': event}
	return render(request, 'TimeTable/eventDesc.html', context)
def authorization(request):
	return render(request, 'TimeTable/authorization.html')

def payment(request):
	return render(request, 'TimeTable/payment.html')
# def detail(request, event_id):
# 	event = get_object_or_404(Event, pk=event_id)
# 	event_serialized = model_to_dict(event)
#     return JsonResponse(json.dumps(event_serialized))

# def all_element(request):
#     events = Event.objects.all()
#     events_serialized = serializers.serialize('json', events)
#     return JsonResponse(events_serialized, safe=False)
class EventView(APIView):
	def get(self, request):
		event = Event.objects.all()
		serializer = EventAllSerializer(event, many=True)
		return Response(serializer.data)

class OrderView(APIView):
	def get(self, request):
		order = Order.objects.all()
		serializer = OrderSerializer(order, many=True)
		return Response(serializer.data)