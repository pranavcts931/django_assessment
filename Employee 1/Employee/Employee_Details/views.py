from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.
def index(request):
    search_query=request.GET.get('department','')
    if search_query:
        data=Employee.objects.filter(department__icontains = search_query)
    else:
        data=Employee.objects.all()
        context={"data":data}
    return render(request,"index.html",{'data':data,'search_query':search_query})

def about(request):
    return render(request,"about.html")

def insertData(request):
    search_query=request.GET.get('department','')
    if search_query:
        data=Employee.objects.filter(department__icontains = search_query)
    else:
        data=Employee.objects.all()
        context={"data":data}
        if request.method=="POST":
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            emp_id=request.POST.get('emp_id')
            email=request.POST.get('email')
            gender=request.POST.get('gender')
            department=request.POST.get('department')
            print(first_name,last_name,emp_id,email,gender,department)
            query=Employee(first_name=first_name,last_name=last_name,emp_id=emp_id,email=email,gender=gender,department=department)
            query.save()
            return redirect("/")
    return render(request,"index.html",{'data':data,'search_query':search_query})

def updateData(request,id):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        emp_id=request.POST.get('emp_id')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        department=request.POST.get('department')
        edit=Employee.objects.get(id=id)
        edit.first_name=first_name
        edit.last_name=last_name
        edit.emp_id=emp_id
        edit.email=email
        edit.gender=gender
        edit.department=department
        edit.save()
        
        return redirect("/")
    d=Employee.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Employee.objects.get(id=id)
    d.delete()
    return redirect("/")
