from django.shortcuts import render

# Create your views here.


def sales(request):
    return render(request, "sales.html")


def salesReturn(request):
    return render(request, "salesReturn.html")
