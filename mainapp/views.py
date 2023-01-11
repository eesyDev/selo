from django.shortcuts import render, redirect
from .models import Banner, Services, Ideas, Feedback, CallBack, Project, Blog

def index(request):
    banners = Banner.objects.all()
    services = Services.objects.all()
    ideas = Ideas.objects.all()
    feedbacks = Feedback.objects.all()

    context = {
        'banners': banners,
        'services': services,
        'ideas': ideas,
        'feedbacks': feedbacks
    }
    return render(request, 'index.html', context)


def add_call_back(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        CallBack.objects.create(
            name = name, 
            email = email, 
            phone = phone, 
            message = message
        )
    return redirect('/')

def about(request):
    project = Project.objects.all()
    context = {'project': project}

    return render(request, 'about.html', context)

def service(request):
    services = Services.objects.all()
    context = {'services': services}

    return render(request, 'service.html', context)


def blog(request):
    articles = Blog.objects.all()
    context = {'articles': articles}
    return render(request, 'blog.html', context)

def contact(request):
    return render(request, 'contact.html')