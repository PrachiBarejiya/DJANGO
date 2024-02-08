from django.shortcuts import render

# Create your views here.
def websitePage(request):
    return render(request,'first.html')