from django.shortcuts import render,redirect
from demoapp.models import Student,StudentForm

# Create your views here.
def homepage(request):
    return render(request,'home.html')

def contactpage(request):
    s=''
    formobj=StudentForm()
    if 'save' in request.POST:
        formobj=StudentForm(request.POST,request.FILES)
        formobj.save()
        s="Successfully Save"
    return render(request,'contact.html',{'ans':s})

def view_data(request):
    stds=Student.objects.all()
    return render(request,'view_data.html',{'stds':stds})

def delete_data(request,del_id):
    print("del===",del_id)
    Student.objects.filter(id=del_id).delete()
    return redirect('/view_data')

def edit_data(request,edit_id):
    obj=Student.objects.filter(id=edit_id).get()

    formobj=StudentForm(instance=obj)
    if 'save' in request.POST:
        formobj=StudentForm(request.POST,request.FILES,instance=obj)
        obj.save()
        # a_name = request.POST['name']
        # a_email = request.POST['email']
        # a_password = request.POST['password']
        # a_contact = request.POST['contact']
        # obj.name=a_name
        # obj.email=a_email
        # obj.password=a_password
        # obj.contact=a_contact
        return redirect('/view_data')
    return render(request,'contact.html',{'obj':obj})

def login(request):
    msg=""
    if 'user_id' in request.session:
        return redirect('/welcome')          
    if 'login' in request.POST:
        email=request.POST['email']
        password=request.POST['password']
        obj=Student.objects.filter(email=email,password=password)
        if obj.count()==1:
            print("Success")
            row=obj.get()
            request.session['user_id']=row.id
            return redirect("/welcome")
        else:
            print("Failure")
            msg="Invalid Email Or Password"
    return render(request,'login.html',{'msg':msg})

def welcome(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    user_id=request.session['user_id']
    print(user_id)
    return render(request,"welcome.html")

def logout(request):
    del request.session['user_id']
    return redirect('/login')