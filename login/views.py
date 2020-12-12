from django.shortcuts import render,redirect
from login.models import Faculties,Class,Schedule,Students,Subject,Week,Attendance,attendImages
import sqlite3,json
from django.contrib import messages
import os.path
import json
from datetime import datetime
from django.utils import timezone
import pytz
import cv2,os
import numpy as np
from PIL import Image
import pickle
from django.conf import settings
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    return render(request, 'start1.html')

def register(request):
    return render(request, 'registration1.html')

def registration(request):
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # db_path = os.path.join(BASE_DIR, "FaceBase.db")
    # Faculties.objects.all()

    faculty = Faculties()
    faculty.FName=request.POST['name']
    faculty.FEmailID = (request.POST['email'])
    faculty.FPassword = request.POST['password']
    print(faculty.FEmailID,faculty.FPassword)
    if request.method=='POST':
        if Faculties.objects.filter(FEmailID=faculty.FEmailID).exists():
            messages.info(request,"user taken")
            print("user taken")
            return redirect('/')
        else:
            faculty.save()
        # q = Faculties(FName="h",FEmailID=Faculties.FEmailID,FPassword=Faculties.FPassword)
        # q.save()
            print(faculty.id)
            print(faculty.FName)
            print(faculty.pk)
            print(Faculties.objects.all())
        # print(TC1_7.objects.filter(id=1))
        # print(TC1_7.objects.get(id=1))
            user = User.objects.create_user(username=faculty.FEmailID,email=faculty.FEmailID,password=faculty.FPassword)
            auth.login(request,user)
            # user.save()
            print("created")
            return redirect('../')
    else :
        return render(request, 'registration1.html')

def showData(request):
    data = Faculties.objects.all()
    print(data)
    return render(request,"showData.html",{"data":data})

def login(request):
    return render(request,"login1.html")

def loggedin(request):
    if request.method == 'POST':
        faculty = Faculties()
        FEmailID = (request.POST['email'])
        print(FEmailID)
        FPassword = request.POST['password']
        print(FPassword)
        user = auth.authenticate(username=FEmailID,password=FPassword)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid')
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def detect(request):
    clas, clasfac = [],[]
    for i in Class.objects.values('ClassName','ClassFaculty_id'):
        clas.append(i['ClassName'])
        clasfac.append(Faculties.objects.filter(id=i['ClassFaculty_id']).values('FEmailID')[0]['FEmailID'])
    classdata = [{"ClassName": c, "ClassFaculty":f} for c,f in zip(clas,clasfac)]
    day = []
    flag = 'a'
    for d in Week.objects.values('WName'):
        day.append(d['WName'])
    if request.method == 'POST':
        idd,sidd,atnd,sttm,edtm = [],[],[],[],[]
        clls,dtt = None,None
        if request.POST.get('clas') and request.POST.get('day') is not None:
            print(request.POST.get('clas'))
            print(request.POST.get('day'))
            for i in Schedule.objects.filter(SClass_id=Class.objects.filter(ClassName=request.POST.get('clas')).values('id')[0]['id'],SWeek_id=Week.objects.filter(WName=request.POST.get('day')).values('id')[0]['id']).values('id'):
                idd.append(i['id'])
            print('show',idd)
            for i in idd:
                sttm.append(Schedule.objects.filter(id=i).values('StartTime')[0]['StartTime'])
                edtm.append(Schedule.objects.filter(id=i).values('EndTime')[0]['EndTime'])
            print('show',idd)
            scheduledata = [{"id":i,"start":mt,"end":mte} for i,mt,mte in zip(idd,sttm,edtm)]
            flag = 'b'
            return render(request, "detector.html",{"flag":flag,"scheduledata":scheduledata,"chosenclass":request.POST['clas'],"chosendate":request.POST['day']})
    return render(request,"detector.html",{"flag":flag,"day":day,"class":clas})

def detected(request):
    print("fileee",request.FILES.get('picture'))
    file2= request.FILES.get('picture')
    fl = attendImages()
    fl.Schedule_id = request.POST.get('schedule')
    fl.Date = timezone.now()
    fl.Image = file2
    fl.save()
    print("file uploaded")
    if request.POST.get('self') == Faculties.objects.filter(id= Schedule.objects.filter(id=request.POST.get('schedule')).values('SFaculty_id')[0]['SFaculty_id']).values('FEmailID')[0]['FEmailID']:
        clas = Schedule.objects.filter(id = request.POST.get('schedule')).values('SClass_id')[0]['SClass_id']
        # print(clas)
        rollno = faceDetection(file2)
        print("detected ",rollno)
        print(request.POST.get('schedule'))
        clasid = Schedule.objects.filter(id = request.POST.get('schedule')).values('SClass_id')[0]['SClass_id']
        print(clasid)
        if request.method == 'POST':
            for c in Students.objects.filter(SClass_id=clasid).values('SID'):
                print("rolll",c['SID'])
                attend = Attendance()
                attend.AStartTime_id = request.POST.get('schedule')
                attend.AClassName_id = Schedule.objects.filter(id = request.POST.get('schedule')).values('SClass_id')[0]['SClass_id']
                attend.AFID_id = Schedule.objects.filter(id = request.POST.get('schedule')).values('SFaculty_id')[0]['SFaculty_id']
                attend.ASID_id = Students.objects.filter(SID=c['SID']).values('id')[0]['id']
                attend.ASubject_id = Schedule.objects.filter(id = request.POST.get('schedule')).values('SSubject_id')[0]['SSubject_id']
                if c['SID'] in rollno:
                    attend.Attend = 1
                else:
                    attend.Attend = 0
                attend.Date = timezone.now()
                # check = Attendance.objects.get(AStartTime_id=attend.AStartTime_id,AClassName_id=attend.AClassName_id,AFID_id=attend.AFID_id,ASID_id=attend.ASID_id,ASubject_id=attend.ASubject_id,Date=attend.Date)
                # print('check',check)
                attend.save()
                # document = Attendance.objects.create(img=file2)
                # document.save()
                messages.info(request,'detected')
            return redirect('/detect')
        return render(request,"detector.html",{"schedule":request.POST.get('schedule')})
    elif request.POST.get('self') is not Faculties.objects.filter(id= Schedule.objects.filter(id=request.POST.get('schedule')).values('SFaculty_id')[0]['SFaculty_id']).values('FEmailID')[0]['FEmailID']:
        messages.info(request,'not valid user')
        return redirect('/detect')
    else:
        return redirect('/detect')
    return redirect('/detect')

def faceDetection(file2):
    detectedFaces = []
    face_cascade = cv2.CascadeClassifier('C:/Users/Administrator/projects/AttendanceProject/login/cascades/data/haarcascade_frontalface_default.xml') 
    cap=cv2.imread("C:/Users/Administrator/projects/AttendanceProject/media/"+str(file2))
    cap=cv2.resize(cap, (760, 760))
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read("C:\\Users\\Administrator\\projects\\AttendanceProject\\login\\recognizer\\tranningData.yml")
    idid=0
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame = cap
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x + w,y + h), (0,0,255), 2)
        idid,conf = rec.predict(gray[y:y+h,x:x+w])
        print(idid)
        if idid != 0:
            if idid not in detectedFaces:
                detectedFaces.append(idid)
            cv2.putText(frame, str(idid),(x,y+h), font,2,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('frame',frame)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return detectedFaces

def datasetCreator(request):
    data = Class.objects.values('ClassName')
    classs = []
    for d in data:
        classs.append(d['ClassName'])
    return render(request,"datasetCreator.html",{"data":data})

def datasetCreated(request):
    student = Students()
    student.SID = request.POST['rollno']
    student.SName = request.POST['name']
    q = Class.objects.filter(ClassName=request.POST['class']).values('id')
    print(q[0]['id'])
    student.SClass_id = q[0]['id']

    if request.method=='POST':
        if Students.objects.filter(SID=student.SID).exists():
            messages.info(request,"user taken")
            print("user taken")
            return redirect('/datasetCreator')
        else:
            # print("path",os.path.dirname())
            sampleNum = 0
            face_cascade = cv2.CascadeClassifier('C:/Users/Administrator/projects/AttendanceProject/login/cascades/data/haarcascade_frontalface_alt2.xml')
            cap = cv2.VideoCapture(0)
            id = request.POST['rollno']
            while(True):
                ret,frame = cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    # print(x,y,w,h)
                    roi_gray = gray[y:y+h, x:x+w]
                    sampleNum = sampleNum + 1
                    cv2.imwrite("C:/Users/Administrator/projects/AttendanceProject/login/dataSet/User."+str(request.POST['rollno'])+"."+str(sampleNum)+".jpg",roi_gray)
                    color = (255,0,0)
                    stroke = 2
                    width = x + w
                    height = y + h
                    cv2.rectangle(frame, (x,y), (width,height), color, stroke)
                    cv2.waitKey(100)
                cv2.imshow('frame',frame)
                # cv2.waitKey(1)
                if(sampleNum>20):
                    break
            cap.release()
            cv2.destroyAllWindows()

            student.save()
            messages.info(request,"saved")
            print(trainer())
            print("created")
            return redirect('/datasetCreator')
    else:
        return redirect('/datasetCreator')
def trainer():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = 'C:/Users/Administrator/projects/AttendanceProject/login/dataSet'
    def getImagesWithID(path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
        faces = []
        IDs = []
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L')
            faceNp = np.array(faceImg,'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1])
            # print("look",os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            print(ID)
            IDs.append(ID)
            cv2.imshow("tranning",faceNp)
            cv2.waitKey(10)
        return np.array(IDs), faces

    IDs, faces=getImagesWithID(path)
    recognizer.train(faces, IDs)
    print(IDs)
    recognizer.save('C:/Users/Administrator/projects/AttendanceProject/login/recognizer/tranningData.yml')
    cv2.destroyAllWindows()
    return "done"

def changeAttendance(request):
    clas, clasfac = [],[]
    for i in Class.objects.values('ClassName','ClassFaculty_id'):
        clas.append(i['ClassName'])
        clasfac.append(Faculties.objects.filter(id=i['ClassFaculty_id']).values('FEmailID')[0]['FEmailID'])
    classdata = [{"ClassName": c, "ClassFaculty":f} for c,f in zip(clas,clasfac)]
    date = []
    for d in Attendance.objects.values('Date'):
        if str(d['Date']).split()[0] not in date:
            date.append(str(d['Date']).split()[0])
        # print(datetime.strptime(c[0]),"%Y-%m-%d")
    # print(date)
    flag='a'
    if request.method == 'POST':
        idd,dataa,sidd,atnd,sttm,edtm,stmid,scheduledata = [],[],[],[],[],[],[],[]
        clls,dtt = None,None
        if request.POST.get('clas') and request.POST.get('date') is not None:
            clls = request.POST.get('clas')
            dtt = request.POST.get('date')
            for i in Attendance.objects.filter(AClassName_id=Class.objects.filter(ClassName=request.POST.get('clas')).values('id')[0]['id']).values('id'):
                if str(Attendance.objects.filter(id=i['id']).values('Date')[0]['Date']).split()[0] == request.POST['date']:
                    idd.append(i['id'])
                    # print(Attendance.objects.filter(id=i['id']).values('AStartTime_id')[0]['AStartTime_id'])
                    if Attendance.objects.filter(id=i['id']).values('AStartTime_id')[0]['AStartTime_id'] not in stmid:
                        stmid.append(Attendance.objects.filter(id=i['id']).values('AStartTime_id')[0]['AStartTime_id'])
            for i in stmid:
                sttm.append(Schedule.objects.filter(id=i).values('StartTime')[0]['StartTime'])
                edtm.append(Schedule.objects.filter(id=i).values('EndTime')[0]['EndTime'])
            print('show',idd,stmid)
            scheduledata = [{"id":i,"start":mt,"end":mte} for i,mt,mte in zip(stmid,sttm,edtm)]
            flag='b'
            return render(request, "changeAttendance.html",{"flag":flag,"scheduledata":scheduledata,"classdata":classdata,"date":date,"chosenclass":request.POST['clas'],"chosendate":request.POST['date'],"data":dataa})
        
        if request.POST.get('schedule') is not None:
            iii,siid,atndd = [],[],[]
            print("print",Class.objects.filter(ClassName=request.POST.get('clsss')).values('id')[0]['id'],request.POST.get('schedule'))
            for i in Attendance.objects.filter(AClassName_id=Class.objects.filter(ClassName=request.POST.get('clsss')).values('id')[0]['id'],AStartTime_id=request.POST.get('schedule')).values('id'):
                if str(Attendance.objects.filter(id=i['id']).values('Date')[0]['Date']).split()[0] == request.POST['dtt']:
                    print(i['id'])
                    iii.append(i['id'])
                    siid.append(Students.objects.filter(id=Attendance.objects.filter(id=i['id']).values('ASID_id')[0]['ASID_id']).values('SID')[0]['SID'])
                    atndd.append(Attendance.objects.filter(id=i['id']).values('Attend')[0]['Attend'])
            sbjt = Subject.objects.filter(id= Attendance.objects.filter(id=iii[0]).values('ASubject_id')[0]['ASubject_id']).values('SubName')[0]['SubName']
            fac = Faculties.objects.filter(id= Attendance.objects.filter(id=iii[0]).values('AFID_id')[0]['AFID_id']).values('FEmailID')[0]['FEmailID']
            schedl = Schedule.objects.filter(id=request.POST.get('schedule')).values('StartTime','EndTime')
            print(schedl[0]['StartTime'],schedl[0]['EndTime'])
            dataa = [{"student":mt,"Attend":mte} for mt,mte in zip(siid,atndd)]
            flag='c'
            return render(request, "changeAttendance.html",{"flag":flag,"scdl":request.POST.get('schedule'),"subjectt":sbjt,"fmail":fac,"end":schedl[0]['EndTime'],"start":schedl[0]['StartTime'],"scheduledata":scheduledata,"classdata":classdata,"date":date,"chosenclass":request.POST.get('clsss'),"chosendate":request.POST.get('dtt'),"data":dataa})
        
        if request.POST.get('clas') and request.POST.get('datte') is not None:
            clls = request.POST.get('clas')
            dtt = request.POST.get('datte')
            for i in Attendance.objects.filter(AClassName_id=Class.objects.filter(ClassName=request.POST.get('clas')).values('id')[0]['id']).values('id'):
                if str(Attendance.objects.filter(id=i['id']).values('Date')[0]['Date']).split()[0] == request.POST['datte']:
                    idd.append(i['id'])
                    # print(Attendance.objects.filter(id=i['id']).values('AStartTime_id')[0]['AStartTime_id'])
                    if Attendance.objects.filter(id=i['id']).values('AStartTime_id')[0]['AStartTime_id'] not in stmid:
                        stmid.append(Attendance.objects.filter(id=i['id']).values('AStartTime_id')[0]['AStartTime_id'])
            for i in stmid:
                sttm.append(Schedule.objects.filter(id=i).values('StartTime')[0]['StartTime'])
                edtm.append(Schedule.objects.filter(id=i).values('EndTime')[0]['EndTime'])
            print('show',idd,stmid)
            scheduledata = [{"id":i,"start":mt,"end":mte} for i,mt,mte in zip(stmid,sttm,edtm)]
            flag='d'
            return render(request, "changeAttendance.html",{"flag":flag,"scheduledata":scheduledata,"classdata":classdata,"date":date,"chosenclass":request.POST['clas'],"chosendate":request.POST['datte'],"data":dataa})
        
        if request.POST.get('schedule1') is not None:
            attndd = []
            for i in Attendance.objects.filter(AStartTime_id=request.POST.get('schedule1')).values('id','Date'):
                if str(i['Date']).split()[0] == request.POST.get('dtt'):
                   attndd.append(i['id'])
            print(attndd)
            flag = 'd'
            for i in attndd:
                obj = Attendance.objects.get(id=i)
                obj.delete()
            return redirect('/changeAttendance')
        if request.POST.get('student') is not None:
            attndd = []
            for i in Attendance.objects.filter(AClassName_id= Class.objects.filter(ClassName=request.POST.get('claas')).values('id')[0]['id'],AStartTime_id=request.POST.get('sidul'),ASID_id = Students.objects.filter(SID=request.POST.get('student')).values('id')[0]['id']).values('id','Date','ASID_id','Attend'):
                if str(i['Date']).split()[0] == request.POST.get('det') and i['ASID_id'] == Students.objects.filter(SID= request.POST.get('student')).values('id')[0]['id']:
                   attndd.append(i['id'])
            print(attndd[0])
            obj = Attendance.objects.get(id=attndd[0])
            obj.Attend = request.POST.get('attend')
            obj.save()            
            return redirect('/changeAttendance')
        return render(request, "changeAttendance.html", {"class":clas, "date":date})
    else:          
        return render(request, "changeAttendance.html", {"class":clas, "date":date})

def showAttendance(request):
    clas, clasfac = [],[]
    for i in Class.objects.values('ClassName','ClassFaculty_id'):
        clas.append(i['ClassName'])
        clasfac.append(Faculties.objects.filter(id=i['ClassFaculty_id']).values('FEmailID')[0]['FEmailID'])
    classdata = [{"ClassName": c, "ClassFaculty":f} for c,f in zip(clas,clasfac)]
    date = []
    for d in Attendance.objects.values('Date'):
        if str(d['Date']).split()[0] not in date:
            date.append(str(d['Date']).split()[0])
        # print(datetime.strptime(c[0]),"%Y-%m-%d")
    # print(date)
    flag = 'a'
    if request.method == 'POST':
        idd,dataa,sidd,atnd,sttm,edtm,stmid,scheduledata = [],[],[],[],[],[],[],[]
        clls,dtt = None,None
        if request.POST.get('clas') and request.POST.get('date') is not None:
            clls = request.POST.get('clas')
            dtt = request.POST.get('date')
            for i in Attendance.objects.filter(AClassName_id=Class.objects.filter(ClassName=request.POST.get('clas')).values('id')[0]['id']).values('id'):
                if str(Attendance.objects.filter(id=i['id']).values('Date')[0]['Date']).split()[0] == request.POST['date']:
                    idd.append(i['id'])
                    # print(Attendance.objects.filter(id=i['id']).values('AStartTime_id')[0]['AStartTime_id'])
                    if Attendance.objects.filter(id=i['id']).values('AStartTime_id')[0]['AStartTime_id'] not in stmid:
                        stmid.append(Attendance.objects.filter(id=i['id']).values('AStartTime_id')[0]['AStartTime_id'])
            for i in stmid:
                sttm.append(Schedule.objects.filter(id=i).values('StartTime')[0]['StartTime'])
                edtm.append(Schedule.objects.filter(id=i).values('EndTime')[0]['EndTime'])
            print('show',idd,stmid)
            scheduledata = [{"id":i,"start":mt,"end":mte} for i,mt,mte in zip(stmid,sttm,edtm)]
            flag = 'b'
            return render(request, "showAttendance.html",{"flag":flag,"scheduledata":scheduledata,"classdata":classdata,"date":date,"chosenclass":request.POST['clas'],"chosendate":request.POST['date'],"data":dataa})
        
        if request.POST.get('schedule') is not None:
            iii,siid,atndd = [],[],[]
            flag = 'c'
            print("print",Class.objects.filter(ClassName=request.POST.get('clsss')).values('id')[0]['id'],request.POST.get('schedule'))
            for i in Attendance.objects.filter(AClassName_id=Class.objects.filter(ClassName=request.POST.get('clsss')).values('id')[0]['id'],AStartTime_id=request.POST.get('schedule')).values('id'):
                if str(Attendance.objects.filter(id=i['id']).values('Date')[0]['Date']).split()[0] == request.POST['dtt']:
                    print(i['id'])
                    iii.append(i['id'])
                    siid.append(Students.objects.filter(id=Attendance.objects.filter(id=i['id']).values('ASID_id')[0]['ASID_id']).values('SID')[0]['SID'])
                    atndd.append(Attendance.objects.filter(id=i['id']).values('Attend')[0]['Attend'])
            sbjt = Subject.objects.filter(id= Attendance.objects.filter(id=iii[0]).values('ASubject_id')[0]['ASubject_id']).values('SubName')[0]['SubName']
            fac = Faculties.objects.filter(id= Attendance.objects.filter(id=iii[0]).values('AFID_id')[0]['AFID_id']).values('FEmailID')[0]['FEmailID']
            schedl = Schedule.objects.filter(id=request.POST.get('schedule')).values('StartTime','EndTime')
            print(schedl[0]['StartTime'],schedl[0]['EndTime'])
            dataa = [{"student":mt,"Attend":mte} for mt,mte in zip(siid,atndd)]
            return render(request, "showAttendance.html",{"flag":flag,"subjectt":sbjt,"fmail":fac,"end":schedl[0]['EndTime'],"start":schedl[0]['StartTime'],"scheduledata":scheduledata,"classdata":classdata,"date":date,"chosenclass":request.POST.get('clsss'),"chosendate":request.POST.get('dtt'),"data":dataa})
        return render(request, "showAttendance.html", {"flag":flag,"class":clas, "date":date})
    else:          
        return render(request, "showAttendance.html", {"flag":flag,"class":clas, "date":date})

def changeClass(request):
    data = Class.objects.values('ClassFaculty_id','ClassName')
    dataa = Faculties.objects.values('id','FEmailID')
    facID,clss,fmail,mail = [],[],[],[]
    # print(data[1]['ClassFaculty_id'],dataa[1]['id'])
    for d in dataa:
        facID.append(d['id'])
        fmail.append(d['FEmailID'])
    for d in data:
        facID.remove(d['ClassFaculty_id'])
        clss.append(d['ClassName'])
    print(facID)
    for e in facID:
        q = Faculties.objects.filter(id=e).values('FEmailID')
        mail.append(q[0]['FEmailID'])
    print(clss)
    print(fmail)
    print(mail)
    return render(request, 'changeClass.html',{"faculty":facID,"class": clss,"fmail":fmail,"mail":mail})

def addClass(request):
    clss = Class()
    clss.ClassName = request.POST['class']
    q = Faculties.objects.filter(FEmailID=request.POST['faculty']).values('id')
    print(q[0]['id'])
    clss.ClassFaculty_id = q[0]['id']
    if request.method == 'POST':
        clss.save()
        messages.info(request,"class added")
    return redirect('/changeClass')

def editClass(request): 
    classs = Class.objects.get(ClassName = request.POST['oldclass'])
    classs.ClassName = request.POST['class']
    if request.method == 'POST':
        classs.save()
        messages.info(request,"class edited")
    return redirect('/changeClass')

def deleteClass(request):
    classs = Class.objects.get(ClassName = request.POST['class'])
    if request.method == 'POST':
        classs.delete()
        messages.info(request,"class deleted")
    return redirect('/changeClass')

def editClassFaculty(request):
    idd = Faculties.objects.filter(FEmailID=request.POST['classfaculty']).values('id')[0]['id']
    cls = Class.objects.get(ClassName = request.POST['class'])
    cls.ClassFaculty_id = idd
    if request.method == 'POST':
        cls.save()
        messages.info(request,"class faculty edited")
    return redirect('/changeClass')

def addFaculty(request):
    faculty = Faculties()
    faculty.FName=request.POST['name']
    faculty.FEmailID = (request.POST['email'])
    faculty.FPassword = request.POST['password']
    if request.method=='POST':
        if Faculties.objects.filter(FEmailID=faculty.FEmailID).exists():
            messages.info(request,"user taken")
            print("user taken")
            return redirect('/')
        else:
            faculty.save()
    return redirect('/changeFaculty')

def changeFaculty(request):
    faculty= Faculties.objects.values('FEmailID')
    fac = []
    for f in faculty:
        fac.append(f['FEmailID'])
    return render(request, "changeFaculty.html",{"data":fac})

def deleteFaculty(request):
    faculty = Faculties.objects.get(FEmailID = request.POST['faculty'])
    if request.method == 'POST':
        faculty.delete()
        messages.info(request,"faculty deleted")
    return redirect('/changeFaculty')

def user(request):
    return render(request,'user.html')

def changeProfile(request):
    # user = User.objects.all()
    # print(user)
    faculty = Faculties.objects.get(FEmailID = request.POST['email'])
    uss = User.objects.get(email = request.POST['email'])
    if request.POST['name'] != '':
        faculty.FName=request.POST['name']
    if request.POST['password'] != '':
        faculty.FPassword = request.POST['password']
        uss.password = request.POST['password']
    if request.method=='POST':   
        faculty.save()
        uss.delete()
        user = User.objects.create_user(username=request.POST['email'],email=request.POST['email'],password=request.POST['password'])
        auth.login(request,user)
    return redirect('/user')

def changeSubject(request):
    idd = Subject.objects.values('SubFaculty_id','SubName')
    iiid = Faculties.objects.values('id')
    ii,iii,sub,fac = [],[],[],[]
    
    for i in iiid:
        ii.append(i['id'])
    print(ii)
    for i in idd:
        ii.remove(i['SubFaculty_id'])
        sub.append(i['SubName'])
        fac.append(Faculties.objects.filter(id = i['SubFaculty_id']).values('FEmailID')[0]['FEmailID'])
    for e in ii:
        q = Faculties.objects.filter(id=e).values('FEmailID')
        iii.append(q[0]['FEmailID'])
    return render(request,"changeSubject.html",{"data":iii,"sub":sub,"ii":fac})

def addSubject(request):
    sub = Subject()
    sub.SubName = request.POST['subject']
    sub.SubFaculty_id = Faculties.objects.filter(FEmailID=request.POST['subfaculty']).values('id')
    if request.method == 'POST':
        sub.save()
        messages.info(request,"subject added")
    return redirect('/changeSubject')

def editSubject(request):
    sub = Subject.objects.get(SubName = request.POST['oldsubject'])
    sub.SubName = request.POST['subject']
    if request.method == 'POST':
        sub.save()
        messages.info(request,"subject edited")
    return redirect('/changeSubject')

def deleteSubject(request):
    sub = Subject.objects.get(SubName = request.POST['subject'])
    if request.method == 'POST':
        sub.delete()
        messages.info(request,"subject deleted")
    return redirect('/changeSubject')

def editSubjectFaculty(request):
    sub = Subject.objects.get(SubName = request.POST['subject'])
    sub.SubFaculty_id = Faculties.objects.filter(FEmailID=request.POST['classfaculty']).values('id')
    if request.method == 'POST':
        sub.save()
        messages.info(request,"subject faculty edited")
    return redirect('/changeSubject')

def changeSchedule(request):
    clas, clasfac = [],[]
    for i in Class.objects.values('ClassName','ClassFaculty_id'):
        clas.append(i['ClassName'])
        clasfac.append(Faculties.objects.filter(id=i['ClassFaculty_id']).values('FEmailID')[0]['FEmailID'])
    classdata = [{"ClassName": c, "ClassFaculty":f} for c,f in zip(clas,clasfac)]
    day = []
    for d in Week.objects.values('WName'):
        day.append(d['WName'])
    flag = 'a'
    subbb = []
    for i in Subject.objects.values('SubName'):
        subbb.append(i['SubName'])
    print("subj",subbb)
    facc = []
    for i in Faculties.objects.values('FEmailID'):
        facc.append(i['FEmailID'])
    # print(Schedule.objects.values_list('StartTime', 'EndTime'))
    data = Schedule.objects.values('id','SClass_id','StartTime','EndTime','SSubject_id','SWeek_id','SFaculty_id')
    idd,classname,subject,week,starttime,endtime,faculty = [],[],[],[],[],[],[]
    dataa = []

    for d in data:
        idd.append(d['id'])
        p = Class.objects.filter(id=d['SClass_id']).values('ClassName')
        classname.append(p[0]['ClassName'])
        starttime.append(d['StartTime'])
        endtime.append(d['EndTime'])
        q = Subject.objects.filter(id=d['SSubject_id']).values('SubName')
        subject.append(q[0]['SubName'])
        r = Week.objects.filter(id=d['SWeek_id']).values('WName')
        week.append(r[0]['WName'])
        v = Faculties.objects.filter(id=d['SFaculty_id']).values('FEmailID')
        faculty.append(v[0]['FEmailID'])
        dataa = [{"id":i, "SClass_name": c, "StartTime": st, "EndTime":et, "SSubject_name":sub, "SWeek_name":wk,"SFaculty_name":fc} for i,c,st,et,sub,wk,fc in zip(idd,classname,starttime,endtime,subject,week,faculty)]
        dataa.append({"id":i, "SClass_name": c, "StartTime": st, "EndTime":et, "SSubject_name":sub, "SWeek_name":wk,"SFaculty_name":fc} for i,c,st,et,sub,wk,fc in zip(idd,classname,starttime,endtime,subject,week,faculty))
        # print(dataa)
    
    return render(request,"changeSchedule.html",{"facul":facc,"sub":subbb,"data":dataa,"flag":flag,"day":day,"classs":clas})

def addSchedule(request):
    schedule = Schedule()
    schedule.StartTime = request.POST['starttime']
    schedule.EndTime = request.POST['endtime']
    schedule.SSubject_id = Subject.objects.filter(SubName=request.POST['subject']).values('id')[0]['id']
    schedule.SWeek_id = Week.objects.filter(WName=request.POST['week']).values('id')[0]['id']
    schedule.SClass_id = Class.objects.filter(ClassName=request.POST['class']).values('id')[0]['id']
    schedule.SFaculty_id = Faculties.objects.filter(FEmailID=request.POST['faculty']).values('id')[0]['id']
    if request.method=='POST':
        if Schedule.objects.filter(StartTime=schedule.StartTime,EndTime=schedule.EndTime,SSubject_id=schedule.SSubject_id,SWeek_id=schedule.SWeek_id,SClass_id=schedule.SClass_id,SFaculty_id=schedule.SFaculty_id).exists():
            messages.info(request,"taken")
        else:
            schedule.save()
            messages.info(request,"schedule added")
    return redirect('/changeSchedule')

def editSchedule(request):
    if request.method == 'POST':
        idd,sidd,atnd,sttm,edtm = [],[],[],[],[]
        clls,dtt = None,None
        if request.POST.get('clas') and request.POST.get('day') is not None:
            print(request.POST.get('clas'))
            print(request.POST.get('day'))
            flag = 'x'
            for i in Schedule.objects.filter(SClass_id=Class.objects.filter(ClassName=request.POST.get('clas')).values('id')[0]['id'],SWeek_id=Week.objects.filter(WName=request.POST.get('day')).values('id')[0]['id']).values('id'):
                idd.append(i['id'])
            print('show',idd)
            for i in idd:
                sttm.append(Schedule.objects.filter(id=i).values('StartTime')[0]['StartTime'])
                edtm.append(Schedule.objects.filter(id=i).values('EndTime')[0]['EndTime'])
            print('show',idd)
            scheduledata = [{"id":i,"start":mt,"end":mte} for i,mt,mte in zip(idd,sttm,edtm)]
            schedule = Schedule.objects.all()
            sub = Subject.objects.values('SubName')
            week = Week.objects.values('WName')
            classs = Class.objects.values('ClassName')
            fac = Faculties.objects.values('FEmailID')
            subb, weekk, claass,facc = [],[],[],[]
            for s in sub:
                subb.append(s['SubName'])
            for w in week:
                weekk.append(w['WName'])
            for c in classs:
                claass.append(c['ClassName'])
            for f in fac:
                facc.append(f['FEmailID'])
            return render(request, "changeSchedule.html",{"sub":subb, "week":weekk, "class":claass,"faculty":facc,"flag":flag,"scheduledata":scheduledata,"chosenclass":request.POST['clas'],"chosendate":request.POST['day']})
    # return render(request,"changeSchedule.html",{"flag":flag,"day":day,"class":clas})
        if request.POST.get('schedule') is not None:
            print(request.POST.get('schedule'))
            sc = Schedule.objects.get(id=request.POST.get('schedule'))
            print(request.POST['starttime'])
            if request.POST['starttime'] != '':
                sc.StartTime = request.POST['starttime']
            if request.POST['endtime'] != '':
                sc.EndTime = request.POST['endtime']
            if request.POST.get('subject') != None:
                sc.SSubject_id = Subject.objects.filter(SubName=request.POST.get('subject')).values('id')[0]['id']
            if request.POST.get('week') != None:
                sc.SWeek_id = Week.objects.filter(WName=request.POST.get('week')).values('id')[0]['id']
            if request.POST.get('class')!= None:
                sc.SClass_id = Class.objects.filter(ClassName=request.POST.get('class')).values('id')[0]['id']
            if request.POST.get('faculty') != None:
            # print(request.POST['faculty'])
                sc.SFaculty_id = Faculties.objects.filter(FEmailID=request.POST.get('faculty')).values('id')[0]['id']
            if request.method == 'POST':
                sc.save()
                messages.info(request,"schedule edited")
            return redirect('/changeSchedule')
        return redirect('/changeSchedule')
    return redirect('/changeSchedule')

def deleteSchedule(request):
    if request.method == 'POST':
        idd,sidd,atnd,sttm,edtm = [],[],[],[],[]
        clls,dtt = None,None
        if request.POST.get('clas') and request.POST.get('day') is not None:
            print(request.POST.get('clas'))
            print(request.POST.get('day'))
            flag = 'y'
            for i in Schedule.objects.filter(SClass_id=Class.objects.filter(ClassName=request.POST.get('clas')).values('id')[0]['id'],SWeek_id=Week.objects.filter(WName=request.POST.get('day')).values('id')[0]['id']).values('id'):
                idd.append(i['id'])
            print('show',idd)
            for i in idd:
                sttm.append(Schedule.objects.filter(id=i).values('StartTime')[0]['StartTime'])
                edtm.append(Schedule.objects.filter(id=i).values('EndTime')[0]['EndTime'])
            print('show',idd)
            scheduledata = [{"id":i,"start":mt,"end":mte} for i,mt,mte in zip(idd,sttm,edtm)]
            return render(request, "changeSchedule.html",{"flag":flag,"scheduledata":scheduledata,"chosenclass":request.POST['clas'],"chosendate":request.POST['day']})
        elif request.POST.get('schedule') is not None:
            sc = Schedule.objects.get(id=request.POST['schedule'])
            if request.method == 'POST':
                sc.delete()
                messages.info(request,"schedule deleted")
    return redirect("/changeSchedule")

def changeStudent(request):
    classs= Class.objects.values('ClassName')
    cl = []
    for c in classs:
        cl.append(c['ClassName'])
    roll = Students.objects.values('SID')
    rn = []
    for r in roll:
        rn.append(r['SID'])
    return render(request,"changeStudent.html", {"class":cl, "rollno":rn})

def editStudent(request):
    stud = Students.objects.get(SID=request.POST['rollno'])
    if request.POST['name'] != '':
        stud.SName = request.POST['name']
    # print(request.POST.get('class'))
    if request.POST.get('class') != None:
        stud.SClass_id = Class.objects.filter(ClassName = request.POST.get('class')).values('id')[0]['id']
    if request.method == 'POST':
        messages.info(request,"edited")
        stud.save()
    return redirect("/changeStudent")

def deleteStudent(request):
    stud = Students.objects.get(SID=request.POST.get('rollno'))
    if request.method == 'POST':
        messages.info(request,"deleted")
        stud.delete()
    return redirect("/changeStudent")

def showData(request):
    clas, clasfac = [],[]
    for i in Class.objects.values('ClassName','ClassFaculty_id'):
        clas.append(i['ClassName'])
        clasfac.append(Faculties.objects.filter(id=i['ClassFaculty_id']).values('FEmailID')[0]['FEmailID'])
    classdata = [{"ClassName": c, "ClassFaculty":f} for c,f in zip(clas,clasfac)]
    # print(classdata)
    sub,subfac = [],[]
    for i in Subject.objects.values('SubName','SubFaculty_id'):
        sub.append(i['SubName'])
        subfac.append(Faculties.objects.filter(id=i['SubFaculty_id']).values('FEmailID')[0]['FEmailID'])
    subjectdata = [{"SubName": c, "SubFaculty":f} for c,f in zip(sub,subfac)]
    # print(subjectdata)
    fname,fac = [],[]
    for i in Faculties.objects.values('FName','FEmailID'):
        fname.append(i['FName'])
        fac.append(i['FEmailID'])
    facultydata = [{"FName": c, "Faculty":f} for c,f in zip(fname,fac)]
    date = []
    for d in Attendance.objects.values('Date'):
        if str(d['Date']).split()[0] not in date:
            date.append(str(d['Date']).split()[0])
    
    flag = 'a'
    if request.method == 'POST':
        sid,sname,studentdata = [],[],[]
        print(request.POST.get('classs'))
        if request.POST.get('classs') is not None:
            # flag = 'b'
            for i in Students.objects.filter(SClass_id=Class.objects.filter(ClassName=request.POST.get('classs')).values('id')[0]['id']).values('SID','SName'):
                sid.append(i['SID'])
                sname.append(i['SName'])
            studentdata = [{"SID":s,"SName":sn} for s,sn in zip(sid,sname)]
            if studentdata != []:
                flag='b'
            return render(request, "showDataa.html",{"flag":flag,"classdata":classdata,"subjectdata":subjectdata,"facultydata":facultydata,"date":date,"studentdata":studentdata})
        
        idd,dataa,sidd,atnd,sttm,edtm,stmid,scheduledata = [],[],[],[],[],[],[],[]
        clls,dtt = None,None
        if request.POST.get('clas') and request.POST.get('date') is not None:
            clls = request.POST.get('clas')
            dtt = request.POST.get('date')
            for i in Attendance.objects.filter(AClassName_id=Class.objects.filter(ClassName=request.POST.get('clas')).values('id')[0]['id']).values('id'):
                if str(Attendance.objects.filter(id=i['id']).values('Date')[0]['Date']).split()[0] == request.POST['date']:
                    idd.append(i['id'])
                    # print(Attendance.objects.filter(id=i['id']).values('AStartTime_id')[0]['AStartTime_id'])
                    if Attendance.objects.filter(id=i['id']).values('AStartTime_id')[0]['AStartTime_id'] not in stmid:
                        stmid.append(Attendance.objects.filter(id=i['id']).values('AStartTime_id')[0]['AStartTime_id'])
            for i in stmid:
                sttm.append(Schedule.objects.filter(id=i).values('StartTime')[0]['StartTime'])
                edtm.append(Schedule.objects.filter(id=i).values('EndTime')[0]['EndTime'])
            print('show',idd,stmid)
            scheduledata = [{"id":i,"start":mt,"end":mte} for i,mt,mte in zip(stmid,sttm,edtm)]
            # if scheduledata != []:
            flag = 'd'
            return render(request, "showDataa.html",{"flag":flag,"scheduledata":scheduledata,"classdata":classdata,"subjectdata":subjectdata,"facultydata":facultydata,"date":date,"chosenclass":request.POST['clas'],"chosendate":request.POST['date'],"data":dataa})
        
        if request.POST.get('schedule') is not None:
            iii,siid,atndd = [],[],[]
            print("print",Class.objects.filter(ClassName=request.POST.get('clsss')).values('id')[0]['id'],request.POST.get('schedule'))
            for i in Attendance.objects.filter(AClassName_id=Class.objects.filter(ClassName=request.POST.get('clsss')).values('id')[0]['id'],AStartTime_id=request.POST.get('schedule')).values('id'):
                if str(Attendance.objects.filter(id=i['id']).values('Date')[0]['Date']).split()[0] == request.POST['dtt']:
                    print(i['id'])
                    iii.append(i['id'])
                    siid.append(Students.objects.filter(id=Attendance.objects.filter(id=i['id']).values('ASID_id')[0]['ASID_id']).values('SID')[0]['SID'])
                    atndd.append(Attendance.objects.filter(id=i['id']).values('Attend')[0]['Attend'])
            sbjt = Subject.objects.filter(id= Attendance.objects.filter(id=iii[0]).values('ASubject_id')[0]['ASubject_id']).values('SubName')[0]['SubName']
            fac = Faculties.objects.filter(id= Attendance.objects.filter(id=iii[0]).values('AFID_id')[0]['AFID_id']).values('FEmailID')[0]['FEmailID']
            schedl = Schedule.objects.filter(id=request.POST.get('schedule')).values('StartTime','EndTime')
            print(schedl[0]['StartTime'],schedl[0]['EndTime'])
            dataa = [{"student":mt,"Attend":mte} for mt,mte in zip(siid,atndd)]
            flag='e'
            return render(request, "showDataa.html",{"flag":flag,"subjectt":sbjt,"fmail":fac,"end":schedl[0]['EndTime'],"start":schedl[0]['StartTime'],"scheduledata":scheduledata,"classdata":classdata,"subjectdata":subjectdata,"facultydata":facultydata,"date":date,"chosenclass":request.POST.get('clsss'),"chosendate":request.POST.get('dtt'),"data":dataa})
        if request.POST.get('class') is not None:
            flag= 'c'
            mid,mst,met,msub,mfac,monday = None,[],[],[],[],[]
            tid,tst,tet,tsub,tfac,tuesday = None,[],[],[],[],[]
            wid,wst,wet,wsub,wfac,wednesday = None,[],[],[],[],[]
            thid,thst,thet,thsub,thfac,thursday = None,[],[],[],[],[]
            fid,fst,fet,fsub,ffac,friday = None,[],[],[],[],[]
            sid,sst,sset,ssub,sfac,saturday = None,[],[],[],[],[]
            for i in Schedule.objects.filter(SClass_id=Class.objects.filter(ClassName=request.POST.get('class')).values('id')[0]['id']).values('StartTime','EndTime','SSubject_id','SWeek_id','SFaculty_id'):
                if i['SWeek_id'] == 1:
                    mid = Week.objects.filter(id=i['SWeek_id']).values('WName')[0]['WName']
                    mst.append(i['StartTime'])
                    met.append(i['EndTime'])
                    msub.append(Subject.objects.filter(id=i['SSubject_id']).values('SubName')[0]['SubName'])
                    mfac.append(Faculties.objects.filter(id=i['SFaculty_id']).values('FEmailID')[0]['FEmailID'])
                if i['SWeek_id'] == 2:
                    tid = Week.objects.filter(id=i['SWeek_id']).values('WName')[0]['WName']
                    tst.append(i['StartTime'])
                    tet.append(i['EndTime'])
                    tsub.append(Subject.objects.filter(id=i['SSubject_id']).values('SubName')[0]['SubName'])
                    tfac.append(Faculties.objects.filter(id=i['SFaculty_id']).values('FEmailID')[0]['FEmailID'])
                if i['SWeek_id'] == 3:
                    wid = Week.objects.filter(id=i['SWeek_id']).values('WName')[0]['WName']
                    wst.append(i['StartTime'])
                    wet.append(i['EndTime'])
                    wsub.append(Subject.objects.filter(id=i['SSubject_id']).values('SubName')[0]['SubName'])
                    wfac.append(Faculties.objects.filter(id=i['SFaculty_id']).values('FEmailID')[0]['FEmailID'])
                if i['SWeek_id'] == 4:
                    thid = Week.objects.filter(id=i['SWeek_id']).values('WName')[0]['WName']
                    thst.append(i['StartTime'])
                    thet.append(i['EndTime'])
                    thsub.append(Subject.objects.filter(id=i['SSubject_id']).values('SubName')[0]['SubName'])
                    thfac.append(Faculties.objects.filter(id=i['SFaculty_id']).values('FEmailID')[0]['FEmailID'])
                if i['SWeek_id'] == 5:
                    fid = Week.objects.filter(id=i['SWeek_id']).values('WName')[0]['WName']
                    fst.append(i['StartTime'])
                    fet.append(i['EndTime'])
                    fsub.append(Subject.objects.filter(id=i['SSubject_id']).values('SubName')[0]['SubName'])
                    ffac.append(Faculties.objects.filter(id=i['SFaculty_id']).values('FEmailID')[0]['FEmailID'])
                if i['SWeek_id'] == 6:
                    sid = Week.objects.filter(id=i['SWeek_id']).values('WName')[0]['WName']
                    sst.append(i['StartTime'])
                    sset.append(i['EndTime'])
                    ssub.append(Subject.objects.filter(id=i['SSubject_id']).values('SubName')[0]['SubName'])
                    sfac.append(Faculties.objects.filter(id=i['SFaculty_id']).values('FEmailID')[0]['FEmailID'])

            monday = [{"start":mt,"end":mte,"sub":ms,"fac":mfc} for mt,mte,ms,mfc in zip(mst,met,msub,mfac)]
            print(monday)
            tuesday = [{"start":mt,"end":mte,"sub":ms,"fac":mfc} for mt,mte,ms,mfc in zip(tst,tet,tsub,tfac)]
            print(tuesday)
            wednesday = [{"start":mt,"end":mte,"sub":ms,"fac":mfc} for mt,mte,ms,mfc in zip(wst,wet,wsub,wfac)]
            print(wednesday)
            thursday = [{"start":mt,"end":mte,"sub":ms,"fac":mfc} for mt,mte,ms,mfc in zip(thst,thet,thsub,thfac)]
            print(thursday)
            friday = [{"start":mt,"end":mte,"sub":ms,"fac":mfc} for mt,mte,ms,mfc in zip(fst,fet,fsub,ffac)]
            print(friday)
            saturday = [{"start":mt,"end":mte,"sub":ms,"fac":mfc} for mt,mte,ms,mfc in zip(sst,sset,ssub,sfac)]
            print(saturday)
            return render(request, "showDataa.html",{"flag":flag,"mid":mid,"tid":tid,"wid":wid,"thid":thid,"fid":fid,"sid":sid,"classdata":classdata,"subjectdata":subjectdata,"facultydata":facultydata,"date":date,"monday":monday,"tuesday":tuesday,"wednesday":wednesday,"thursday":thursday,"friday":friday,"saturday":saturday})
        return render(request, "showDataa.html",{"flag":flag,"classdata":classdata,"subjectdata":subjectdata,"facultydata":facultydata,"date":date})
    else:
        # print(studentdata)
        return render(request, "showDataa.html",{"flag":flag,"classdata":classdata,"subjectdata":subjectdata,"facultydata":facultydata,"date":date})

def manualAttendance(request):
    clas, clasfac = [],[]
    for i in Class.objects.values('ClassName','ClassFaculty_id'):
        clas.append(i['ClassName'])
        clasfac.append(Faculties.objects.filter(id=i['ClassFaculty_id']).values('FEmailID')[0]['FEmailID'])
    classdata = [{"ClassName": c, "ClassFaculty":f} for c,f in zip(clas,clasfac)]
    day = []
    for d in Week.objects.values('WName'):
        day.append(d['WName'])
    flag = 'a'
    if request.method == 'POST':
        idd,sidd,atnd,sttm,edtm = [],[],[],[],[]
        clls,dtt = None,None
        if request.POST.get('clas') and request.POST.get('day') is not None:
            print(request.POST.get('clas'))
            print(request.POST.get('day'))
            flag = 'b'
            for i in Schedule.objects.filter(SClass_id=Class.objects.filter(ClassName=request.POST.get('clas')).values('id')[0]['id'],SWeek_id=Week.objects.filter(WName=request.POST.get('day')).values('id')[0]['id']).values('id'):
                idd.append(i['id'])
            print('show',idd)
            for i in idd:
                sttm.append(Schedule.objects.filter(id=i).values('StartTime')[0]['StartTime'])
                edtm.append(Schedule.objects.filter(id=i).values('EndTime')[0]['EndTime'])
            print('show',idd)
            scheduledata = [{"id":i,"start":mt,"end":mte} for i,mt,mte in zip(idd,sttm,edtm)]
            return render(request, "manualAttendance.html",{"flag":flag,"scheduledata":scheduledata,"chosenclass":request.POST['clas'],"chosendate":request.POST['day']})
    return render(request,"manualAttendance.html",{"flag":flag,"day":day,"class":clas})

def attend(request):
    if request.POST.get('self') == Faculties.objects.filter(id= Schedule.objects.filter(id=request.POST.get('schedule')).values('SFaculty_id')[0]['SFaculty_id']).values('FEmailID')[0]['FEmailID']:
        clas = Schedule.objects.filter(id = request.POST.get('schedule')).values('SClass_id')[0]['SClass_id']
        # print(clas)
        stud = []
        print(Students.objects.filter(SClass_id=clas).values('SID'))
        for c in Students.objects.filter(SClass_id=clas).values('SID'):
            print('did: ',c['SID'])
            stud.append(c['SID'])
        # print(stud)
        flag='c'
        return render(request,"manualAttendance.html",{"flag":flag,"data":stud,"schedule":request.POST.get('schedule')})
    elif request.POST.get('self') is not Faculties.objects.filter(id= Schedule.objects.filter(id=request.POST.get('schedule')).values('SFaculty_id')[0]['SFaculty_id']).values('FEmailID')[0]['FEmailID']:
        messages.info(request,'not valid user')
        return redirect('/manualAttendance')
    else:
        return redirect('/manualAttendance')

def attended(request):
    print(request.POST.get('schedule'))
    rollno = request.POST.getlist('rollno[]')
    print(rollno)
    clasid = Schedule.objects.filter(id = request.POST.get('schedule')).values('SClass_id')[0]['SClass_id']
    print(clasid)
    if request.method == 'POST':
        for c in Students.objects.filter(SClass_id=clasid).values('SID'):
            print(c['SID'])
            attend = Attendance()
            attend.AStartTime_id = request.POST.get('schedule')
            attend.AClassName_id = Schedule.objects.filter(id = request.POST.get('schedule')).values('SClass_id')[0]['SClass_id']
            attend.AFID_id = Schedule.objects.filter(id = request.POST.get('schedule')).values('SFaculty_id')[0]['SFaculty_id']
            attend.ASID_id = Students.objects.filter(SID=c['SID']).values('id')[0]['id']
            attend.ASubject_id = Schedule.objects.filter(id = request.POST.get('schedule')).values('SSubject_id')[0]['SSubject_id']
            if str(c['SID']) in rollno:
                attend.Attend = 1
            else:
                attend.Attend = 0
            attend.Date = timezone.now()
            attend.save()
    return redirect("/manualAttendance")