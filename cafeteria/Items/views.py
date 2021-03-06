from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import *
from .functions import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ItemSerializer, NonStockSerializer
from django.urls import reverse



def addItem(request):
    if request.method== "POST":
        if request.POST.get("save-button"):
            print("save button save button save button save button ")
            if ItemsAdd(request):
                print("item added success")
                return HttpResponseRedirect(reverse("addItem"))

        if request.POST.get("cancel-button"):
            return HttpResponseRedirect(reverse("addItem"))
        
        if request.POST.get("update-button"):
            print("update update update update update update button")
            UpdateItem(request)
            return HttpResponseRedirect(reverse("addItem"))

    else:
        return render(request, "addItem.html", {'addItems': Items.objects.all()})


def addNonStockItem(request):
    if request.method== "POST":
        if request.POST.get("save-button"):
            print("save button save button save button save button ")
            if addNonStockItems(request):
                print("item added success")
                return HttpResponseRedirect(reverse("addNonStockItem"))

        if request.POST.get("cancel-button"):
           return HttpResponseRedirect(reverse("addNonStockItem"))
        
        if request.POST.get("update-button"):
            print("update update update update update update button")
            updateNonStockItems(request)
            return HttpResponseRedirect(reverse("addNonStockItem"))


    else:
        return render(request, "addNonStockItem.html", {'nonStock': NonStock.objects.all()})











def pos(request):
    return render(request, "pos.html")

def barcodeLabel(request):
    return render(request, "barcodeLabel.html")

# api work
# api for items searching
@api_view(['GET'])
def SearchByItemField(request):
    field=request.GET.get("field")
    value=request.GET.get("value")
    print(field,value)
    try:
        if field=="Name":
            return Response(ItemSerializer(Items.objects.filter(
                        item_name__icontains=value).order_by('-id'),
                        many=True).data)
        elif field=="Code":
            return Response(ItemSerializer(Items.objects.filter(
                        item_code__icontains=value).order_by('-id'),
                        many=True).data)
    except Exception as e:
        return Response({"message":"No data found {}".format(e)})


# api for non-stock search items
@api_view(['GET'])
def SearchByStockField(request):
    field=request.GET.get("field")
    value=request.GET.get("value")
    print(field,value)
    try:
        if field=="Name":
            return Response(NonStockSerializer(NonStock.objects.filter(
                        nonStock_item_name__icontains=value).order_by('-id'),
                        many=True).data)
        elif field=="Code":
            return Response(NonStockSerializer(NonStock.objects.filter(
                        nonStock_item_code__icontains=value).order_by('-id'),
                        many=True).data)
    except Exception as e:
        return Response({"message":"No data found {}".format(e)})


@api_view(['GET'])
def UpdateItemQueryCall(request):
    value=request.GET.get("id")
    try:
        return Response(ItemSerializer(Items.objects.filter(id=value),many=True).data)
    except Exception as e:
        return Response({"message":"No data found {}".format(e)})


@api_view(['GET'])
def UpdateNonStockQueryCall(request):
    value=request.GET.get("nonStock-id")
    try:
        return Response(NonStockSerializer(NonStock.objects.filter(id=value),many=True).data)
    except Exception as e:
        return Response({"message":"No data found {}".format(e)})

