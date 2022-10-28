from django.contrib import admin

from task.models import Feedbacks, Question,sesion

# Register your models here.
admin.site.register(Question)
admin.site.register(Feedbacks)
admin.site.register(sesion)