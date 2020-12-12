from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.index, name='index'),
    path('register',views.register, name='register'),
    path('registration',views.registration, name='registration'),
    path('view',views.showData,name='view'),
    path('login',views.login,name='login'),
    path('loggedin',views.loggedin,name='loggedin'),
    path('logout',views.logout,name='logout'),
    path('user',views.user,name='user'),
    # path('detector',views.detect,name="detect"),
    path('detect',views.detect,name="detect"),
    path('detected',views.detected,name="detected"),
    path('datasetCreator',views.datasetCreator,name="datasetCreator"),
    path('datasetCreated',views.datasetCreated,name="datasetCreated"),
    path('showAttendance',views.showAttendance,name="showAttendance"),
    path('changeClass',views.changeClass,name="changeClass"),
    path('addClass',views.addClass,name="addClass"),
    path('editClass',views.editClass,name="editClass"),
    path('deleteClass',views.deleteClass,name="deleteClass"),
    path('editClassFaculty',views.editClassFaculty,name="editClassFaculty"),
    path('changeFaculty',views.changeFaculty,name="changeFaculty"),
    path('addFaculty',views.addFaculty,name="addFaculty"),
    path('deleteFaculty',views.deleteFaculty,name="deleteFaculty"),
    path('changeProfile',views.changeProfile,name="changeProfile"),
    path('changeSubject',views.changeSubject,name="changeSubject"),
    path('addSubject',views.addSubject,name="addSubject"),
    path('editSubject',views.editSubject,name="editSubject"),
    path('deleteSubject',views.deleteSubject,name="deleteSubject"),
    path('editSubjectFaculty',views.editSubjectFaculty,name="editSubjectFaculty"),
    path('changeSchedule',views.changeSchedule,name="changeSchedule"),
    path('addSchedule',views.addSchedule,name="addSchedule"),
    path('editSchedule',views.editSchedule,name="editSchedule"),
    path('deleteSchedule',views.deleteSchedule,name="deleteSchedule"),
    path('changeStudent',views.changeStudent,name="changeStudent"),
    path('editStudent',views.editStudent,name="editStudent"),
    path('deleteStudent',views.deleteStudent,name="deleteStudent"),
    path('showData',views.showData, name="showData"),
    path('manualAttendance',views.manualAttendance, name="manualAttendance"),
    path('attend',views.attend,name="attend"),
    path('attended',views.attended,name="attended"),
    path('changeAttendance',views.changeAttendance,name="changeAttendance"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# workon project
# python manage.py runserver