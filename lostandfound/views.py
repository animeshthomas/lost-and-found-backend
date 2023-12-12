from django.shortcuts import render
from .serializer import ItemSerializer
from .models import Item
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def addLostFound(request):
   if request.method == 'POST':
       rdata = json.loads(request.body)
       serializer = ItemSerializer(data=rdata)
       if serializer.is_valid():
           serializer.save()
           return HttpResponse(json.dumps({"status":"Item added successfully"}))
       else:
           return HttpResponse(json.dumps({"status":"Item not added"}))

@csrf_exempt
def getLostFound(request):
    if request.method=='POST':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return HttpResponse(json.dumps(serializer.data))

@csrf_exempt
def searchLostFound(request):
    if request.method=='POST':
        return HttpResponse(json.dumps({"status":"Item deleted successfully"}))

def deleteLostFound(request):
    if request.method=='POST':
        
        return HttpResponse(json.dumps({"status":"Item deleted successfully"}))


# Create your views here.
