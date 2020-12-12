from django.contrib import admin
from .models import Faculties
from .models import Class
from .models import Week
from .models import Subject
from .models import Students
from .models import Schedule
from .models import Attendance
# Register your models here.
admin.site.register(Faculties)
admin.site.register(Class)
admin.site.register(Week)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(Students)
admin.site.register(Attendance)