from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Subquery
import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.


def index(request):
    education = educationalOffering.objects.all()
    news = newsAndUpdates.objects.all()
    images = homeSlider.objects.all()
    testimonial = testimonials.objects.all()
    academy=academyWorks.objects.all()
    return render(request,'index.html',{'educationalOffering':education,'academy':academy,'news':news,'images':images,'testimonial':testimonial})

def about(request):
    return render(request,'about.html')

def visionMission(request):
    education = educationalOffering.objects.all()
    vision = visionAndMission.objects.get(category="VISION")
    mission = visionAndMission.objects.get(category="MISSION")
    return render(request,'visionMission.html',{'vision':vision,'mission':mission,'educationalOffering':education})

def chancellorMessag(request):
    education = educationalOffering.objects.all()
    chancellorMessages = chancellorMessage.objects.all()
    return render(request,'chancellorsMessage.html',{'data':chancellorMessages,'educationalOffering':education})


def facultys(request):
    education = educationalOffering.objects.all()
    f = faculty.objects.all()
    return render(request,'faculty.html',{'faculties':f,'educationalOffering':education})

def departments(request):
    return render(request,'404.html')
def thesisPolicys(request):
    education = educationalOffering.objects.all()
    t = thesisPolicy.objects.all()
    return render(request,'thesisPolicy.html',{'thesis':t,'educationalOffering':education})


def gradingSystems(request):
    grades = gradeTable.objects.all()
    thesis = thesisEvaluation.objects.all()
    return render(request,'gradingSystem.html',{'grades':grades,'thesisEvaluation':thesis})

def requirement(request):
    education = educationalOffering.objects.all()
    return render(request,'requirement.html',{'educationalOffering':education})

def refundPolicy(request):
    education = educationalOffering.objects.all()
    steps = refundSteps.objects.all()
    charges= refundCharges.objects.all()
    return render(request,'refundPolicy.html',{'educationalOffering':education,'steps':steps,'charges':charges})

def nonDiscriminationPolicys(request):
    education = educationalOffering.objects.all()
    policies = nonDiscriminationPolicy.objects.all()
    return render(request,'nonDiscriminationPolicy.html',{'educationalOffering':education,'policies':policies})



def education(request,id):
    education = educationalOffering.objects.get(id=id)
    course= degreeProgram.objects.filter(educationalOffering = education)
    educationDegree = educationalOffering.objects.all()
    dictionary,mainList={},[]
    if course:
        if course[0].specializationAvailable:
            for i in course:
                specializationCourses = specialization.objects.filter(degreeProgram = i)
                dictionary = {"heading":specializationCourses[0].degreeProgram.name,"specializations":specializationCourses}
                mainList.append(dictionary)
            acceptanceCriteria = acceptancePolicy.objects.filter(educationalOffering=education)
            nominationConsideratio = nominationConsideration.objects.filter(educationalOffering=education)
            print(mainList)
            context={
                'specialization':mainList,
                'heading':education,
                'acceptanceCriteria':acceptanceCriteria,
                'nominationConsideration':nominationConsideratio,
                'educationalOffering':educationDegree,
                
            }
            return render(request,'test.html',context)
            
        elif  eligibilityHeader.objects.filter(degreeProgram = course[0]).exists():
            for i in course:
                eligibilityHead = eligibilityHeader.objects.get(degreeProgram = i)
                eligibilityDetail = eligibilityDetails.objects.filter(eligibiltyHeader=eligibilityHead)
                dictionary = {
                    "heading":eligibilityHead.heading,
                    "subHeading":eligibilityHead.description,
                    'eligibilities' : eligibilityDetail
                }
                mainList.append(dictionary)
            acceptancePolicies = acceptancePolicy.objects.filter(educationalOffering=education)
            context = {
                'postDoctoral' : True,
                'heading':education,
                'mainList':mainList,
                'courses': course,
                'acceptancePolicies': acceptancePolicies,
                'educationalOffering':educationDegree
            }
            return render(request,'test.html',context)
    
    else:
        context = {
            'educationalOffering':educationDegree
        }
        return render(request,'404.html',context)
    

def accreditation(request):
    education = educationalOffering.objects.all()
    para = accreditationParagraph.objects.all()[0]
    lists = accreditationList.objects.all()
    return render(request,'accreditation.html',{'para':para,'lists':lists,'educationalOffering':education})

def describingAccreditations(request):
    education = educationalOffering.objects.all()
    mainList=[]
    para = describingAccreditationParagraph.objects.filter(listAvailable=False)[0]
    paraTrue = describingAccreditationParagraph.objects.filter(listAvailable=True)
    for i in paraTrue:
        dictionary={}
        data = describingAccreditation.objects.filter(heading=i)
        dictionary['heading'] = data[0].heading
        dictionary['contentList'] = data     
        mainList.append(dictionary)
    print(mainList)
    return render(request,'describingAccreditation.html',{'para':para,'lists':mainList,'educationalOffering':education})

def afterGraduationServicesFunction(request):
    education = educationalOffering.objects.all()
    services = afterGraduationServices.objects.all()
    return render(request,'afterGraduationServices.html',{'lists':services,'educationalOffering':education})


def studentFilesPolicys(request):
    data = studentFiles.objects.all()
    return render(request,'studentFilesPolicy.html',{'data':data})


def educationModels(request):
    education = educationalOffering.objects.all()
    category = educationModel.objects.all().order_by('title')
    data1 = educationalModalContent.objects.filter(title=category[0])
    data2 = educationalModalContent.objects.filter(title=category[1])
    data3 = educationalModalContent.objects.filter(title=category[2])
    offers = universityOffering.objects.all()
    education = educationalOffering.objects.all()
    for i in education:
        course= degreeProgram.objects.filter(educationalOffering = i)
        educationDegree = educationalOffering.objects.all()
        dictionary,mainList={},[]
        if course:
            if course[0].specializationAvailable:
                for i in course:
                    specializationCourses = specialization.objects.filter(degreeProgram = i)
                    dictionary = {"heading":specializationCourses[0].degreeProgram.name,"specializations":specializationCourses}
                    mainList.append(dictionary)
                print(mainList)
    context={
        'offer':offers,
        'data1':data1,
        'heading1':data1[0].title,
        'heading2':data2[0].title,
        'heading3':data3[0].title,
        'data2':data2,
        'data3':data3,
        'education':education,
        'lol' : mainList,
        'educationalOffering':education
        }
    return render(request,'educationModel.html',context)


def gallerys(request):
    galler = gallery.objects.all()
    return render(request,'gallery.html',{'gallery':galler})

def contact(request):
    data = accreditatedCenters.objects.all()
    centers = academicsCenters.objects.all()
    education = educationalOffering.objects.all()
    main = mainCampus.objects.all()
    return render(request,'contact.html',{'accreditatedCenters':data,'centers':centers,'educationalOffering':education,'main':main})

def contactQueryView(request):
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact_number']
    country = request.POST['country']
    message = request.POST['message']
    contactQuery(
        name=name,
        email=email,
        contactNumber=contact,
        country = country,
        message= message,
        createDate =  datetime.datetime.now()
    ).save();

    send_mail(
    'Contact Query From Website',
    message,
    'vyasaniket6@gmail.com',
    [email],
   )
    return redirect('/')

def login(request):
    if request.method=="POST":
        email = request.POST['user']
        pas = request.POST['pass']
        user = auth.authenticate(username=email,password=pas)
        if user is not None:
            auth.login(request,user)
            if user.is_superuser:
                return redirect('/admin')
            else:
                return redirect('/dashboard')
        else:
            messages.error(request,'bad credentials!!!')
            return redirect('/',{'error':True})