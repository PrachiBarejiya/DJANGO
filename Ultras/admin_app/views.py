from django.shortcuts import render,redirect
from admin_app.models import contact

# Create your views here.

def log(request):
    if 'user_id' in request.session:
        return redirect('/view-data')
    if 'login' in request.POST:
        email=request.POST['email']
        password=request.POST['password']
        obj=contact.objects.filter(email=email,password=password)
        if obj.count()==1:
            print("Sucess")
            row=obj.get()
            request.session['user_id']=row.id
            return redirect('/dashboard')
        else:
            print("failure")
           
    
    return render(request,'login1.html')
def ct(request):
    s=''
    if 'save' in request.POST:
        a_name=request.POST['name']
        a_email=request.POST['email']
        a_password=request.POST['password']
        a_contact=request.POST['contact']
        obj=contact(
            name=a_name,
            email=a_email,
            password=a_password,
            contact=a_contact,
        )
        obj.save()
        s="Created"
        return redirect('/dashboard')
    return render(request,'ct.html',{'s':s})
def dashboard(request):
    return render(request,'dashboard.html')

def slider(request):
    return render(request,'slider.html')

# def dashboard(request):
   
   
