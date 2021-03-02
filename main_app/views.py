from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Subquery
import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.


def index(request):
    education = educationalOffering.objects.all().order_by('priority')
    spec = specialization.objects.all()
    programs = degreeProgram.objects.all()
    news = newsAndUpdates.objects.all()
    images = homeSlider.objects.all()
    testimonial = testimonials.objects.all()
    academy=academyWorks.objects.all()
    mainList=[]
    mainList1 = []
    for i in education:
        dictionaryList , dictionaryTab = {},{}
        prog = degreeProgram.objects.filter(educationalOffering=education)
        dictionaryList = {
            'program':education,
            'degrees':prog
        }
        dictionaryTab = {
            'degrees':prog
        }
        mainList.append(dictionaryList)
        mainList1.append(dictionaryTab)
    return render(request,'index.html',{'mainList1':mainList1,'mainList':mainList,'spec':spec,'degree':programs,'educationalOffering':education,'academy':academy,'news':news,'images':images,'testimonial':testimonial})


def visionMission(request):
    education = educationalOffering.objects.all().order_by('priority')
    vision = visionAndMission.objects.get(category="VISION")
    mission = visionAndMission.objects.get(category="MISSION")
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    return render(request,'visionMission.html',{'spec':spec,'degree':program,'vision':vision,'mission':mission,'educationalOffering':education,'spec':spec})

def chancellorMessag(request):
    education = educationalOffering.objects.all().order_by('priority')
    chancellorMessages = chancellorMessage.objects.all()
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    return render(request,'chancellorsMessage.html',{'spec':spec,'degree':program,'data':chancellorMessages,'educationalOffering':education})


def facultys(request):
    education = educationalOffering.objects.all().order_by('priority')
    f = faculty.objects.all()
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    return render(request,'faculty.html',{'faculties':f,'educationalOffering':education,'spec':spec,'degree':program})

def departments(request):
    try:
        spec = specialization.objects.all()
        program = degreeProgram.objects.all()
        return render(request,'departments.html',{'spec':spec,'degree':program})
    except:
        return redirect('/404')



def thesisPolicys(request):
    education = educationalOffering.objects.all().order_by('priority')
    t = thesisPolicy.objects.all()
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    return render(request,'thesisPolicy.html',{'thesis':t,'educationalOffering':education,'spec':spec,'degree':program})


def gradingSystems(request):
    education = educationalOffering.objects.all().order_by('priority')
    grades = gradeTable.objects.all()
    thesis = thesisEvaluation.objects.all()
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    return render(request,'gradingSystem.html',{'grades':grades,'educationalOffering':education,'thesisEvaluation':thesis,'spec':spec,'degree':program})

def requirement(request):
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    education = educationalOffering.objects.all().order_by('priority')
    header = requirementHeader.objects.all()
    mainList=[]
    for i in header:
        dictionary = {}
        content = requirementContent.objects.filter(header=i)
        dictionary={'header':i,'content':content}
        mainList.append(dictionary)
    print(mainList)
    return render(request,'requirement.html',{'educationalOffering':education,'spec':spec,'degree':program,'data':mainList})

def refundPolicy(request):
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    education = educationalOffering.objects.all().order_by('priority')
    steps = refundSteps.objects.all()
    charges= refundCharges.objects.all()
    return render(request,'refundPolicy.html',{'educationalOffering':education,'steps':steps,'charges':charges,'spec':spec,'degree':program})

def nonDiscriminationPolicys(request):
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    education = educationalOffering.objects.all().order_by('priority')
    policies = nonDiscriminationPolicy.objects.all()
    return render(request,'nonDiscriminationPolicy.html',{'educationalOffering':education,'policies':policies,'spec':spec,'degree':program})



def education(request,id):
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    education = educationalOffering.objects.get(id=id)
    course= degreeProgram.objects.filter(educationalOffering = education)
    educationDegree = educationalOffering.objects.all().order_by('priority')
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
                'spec':spec,'degree':program

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
                'educationalOffering':educationDegree,
                'spec':spec,'degree':program
            }
            return render(request,'test.html',context)

    else:
        spec = specialization.objects.all()
        program = degreeProgram.objects.all()
        context = {
            'educationalOffering':educationDegree,
            'spec':spec,'degree':program
        }
        return redirect('/404',context)


def accreditation(request):
    education = educationalOffering.objects.all().order_by('priority')
    para = accreditationParagraph.objects.all()[0]
    lists = accreditationList.objects.all()
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    return render(request,'accreditation.html',{'para':para,'lists':lists,'educationalOffering':education,'spec':spec,'degree':program})

def describingAccreditations(request):
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    education = educationalOffering.objects.all().order_by('priority')
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
    return render(request,'describingAccreditation.html',{'para':para,'lists':mainList,'educationalOffering':education,'spec':spec,'degree':program})

def afterGraduationServicesFunction(request):
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    education = educationalOffering.objects.all().order_by('priority')
    services = afterGraduationServices.objects.all()
    return render(request,'afterGraduationServices.html',{'lists':services,'educationalOffering':education,'spec':spec,'degree':program})


def studentFilesPolicys(request):
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    data = studentFiles.objects.all()
    education = educationalOffering.objects.all().order_by('priority')
    return render(request,'studentFilesPolicy.html',{'data':data,'spec':spec,'degree':program,'educationalOffering':education,})


def educationModels(request):
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    education = educationalOffering.objects.all().order_by('priority')
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
        'educationalOffering':education,
        'spec':spec,'degree':program,
        }
    return render(request,'educationModel.html',context)


def gallerys(request):
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    galler = gallery.objects.all()
    paginator = Paginator(galler,9)
    page = request.GET.get('page')
    galler = paginator.get_page(page)
    ducation = educationalOffering.objects.all().order_by('priority')
    return render(request,'gallery.html',{'educationalOffering':ducation,'gallery':galler,'spec':spec,'degree':program,})

def contact(request):
    spec = specialization.objects.all()
    program = degreeProgram.objects.all()
    data = accreditatedCenters.objects.all().order_by('-id')
    centers = academicsCenters.objects.all()
    education = educationalOffering.objects.all().order_by('priority')
    main = mainCampus.objects.all()
    return render(request,'contact.html',{'spec':spec,'degree':program,'accreditatedCenters':data,'centers':centers,'educationalOffering':education,'main':main})

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


def notFound(request):
    context={
        'education':educationalOffering.objects.all().order_by('priority')
        }
    return render(request,'404.html',context)