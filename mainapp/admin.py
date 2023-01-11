from django.contrib import admin
from .models import Banner, Ideas, Feedback, Services, CallBack, Subscribtion, Project, Blog
# Register your models here.


admin.site.register(Banner)
admin.site.register(Services)
admin.site.register(Feedback)
admin.site.register(CallBack)
admin.site.register(Subscribtion)
admin.site.register(Ideas)
admin.site.register(Project)
admin.site.register(Blog)