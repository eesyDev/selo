from django.urls import path
from .views import index, add_call_back, about, service, blog, contact


urlpatterns = [
    path('', index, name='home'),
    path('add_call_back', add_call_back, name='add_call_back'),
    path('about_us', about, name='about'),
    path('service', service, name='service'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact')
]