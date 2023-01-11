from django.shortcuts import render
from .models import Banner, Services, Ideas, Feedback, CallBack

def index(request):
    banners = Banner.objects.all()
    services = Services.objects.all()
    ideas = Ideas.objects.all()
    feedbacks = Feedback.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

    # callback = CallBack(
    #     name = name, email = email, phone = phone, message = message
    # )
    context = {
        'banners': banners,
        'services': services,
        'ideas': ideas,
        'feedbacks': feedbacks
        # 'callbacks': callback
    }
    return render(request, 'index.html', context)

