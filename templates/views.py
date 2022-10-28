from django.shortcuts import render, HttpResponse

# Create your views here.
def vol(request):
    return render(request, 'fine.html')