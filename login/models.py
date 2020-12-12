from django.db import models

# Create your models here.
# class TC1_7(models.Model):
    
#     Name = models.CharField(max_length=200)
#     Age = models.IntegerField()
#     Attendance = models.BooleanField()

#     def __str__(self):
#         return self.Name

class Faculties(models.Model):
    FName = models.CharField(max_length=200)
    FEmailID = models.EmailField(max_length=200)
    FPassword = models.CharField(max_length=20)

    def __str__(self):
        return self.FName
    def __str__(self):
        return self.FEmailID
    def __str__(self):
        return self.FPassword

class Class(models.Model):
    ClassName = models.CharField(max_length=200)
    ClassFaculty = models.ForeignKey(Faculties,on_delete=models.CASCADE,null=True)

class Week(models.Model):
    WName = models.CharField(max_length=20)

class Subject(models.Model):
    SubName = models.CharField(max_length=200)
    SubFaculty = models.ForeignKey(Faculties,on_delete=models.CASCADE,null=True)

class Students(models.Model):
    SID = models.BigIntegerField()
    SName = models.CharField(max_length=200)
    SClass = models.ForeignKey(Class,on_delete=models.CASCADE,null=True)

class Schedule(models.Model):
    SWeek = models.ForeignKey(Week,on_delete=models.CASCADE,null=True)
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    SSubject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    SClass = models.ForeignKey(Class,on_delete=models.CASCADE,null=True)
    SFaculty = models.ForeignKey(Faculties,on_delete=models.CASCADE,null=True)

class Attendance(models.Model):
    ASID = models.ForeignKey(Students,on_delete=models.CASCADE,null=True)
    AFID = models.ForeignKey(Faculties,on_delete=models.CASCADE,null=True)
    AClassName = models.ForeignKey(Class,on_delete=models.CASCADE,null=True)
    ASubject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    AStartTime = models.ForeignKey(Schedule,on_delete=models.CASCADE,null=True)
    Date = models.DateTimeField()
    Attend = models.BooleanField(default=False)
    # img = models.FileField(upload_to='pics',null=True)

class attendImages(models.Model):
    Schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE,null=True)
    Date = models.DateTimeField(null=True)
    Image = models.FileField(null=True)
    