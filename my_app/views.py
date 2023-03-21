from django.shortcuts import render,redirect

from .models import Student

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')


def home(request):
    return render(request, 'my_app/home.html')

def add(request):
    
    if request.method == "POST":
        student = Student()
        student.roll = request.POST['roll']
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.address = request.POST['address']
        student.phone = request.POST['phone']
        student.save()
        return redirect('home')
    return render(request, 'my_app/add.html')