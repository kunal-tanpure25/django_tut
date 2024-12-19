from django.shortcuts import render , HttpResponse
from home.models import Form

# Create your views here.

def index(request):
    context = {
        'title': 'Home',
        'message': 'Welcome to my website',
        'age' : 25
    }
    return render(request , 'index.html' , context)

def about(request):
    return render(request , 'about.html')

def contact(request):
    return HttpResponse("mail  : Kunaltanpured4@gmail.com")

def signup(request):
    return render(request , 'login.html')

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        form = Form(name = name , email = email , contact = contact , feedback = feedback)
        form.save()
    
    return render(request , 'form.html')

def thanks(request):
    return HttpResponse(request , 'thanks.html')