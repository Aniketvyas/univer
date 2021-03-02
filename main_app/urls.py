
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.index),
    path('index',views.index),
    path('visionMission',views.visionMission),
    path('chancellorsMessage',views.chancellorMessag),
    path('faculty',views.facultys),
    path('departments',views.departments),
    path('thesisPolicy',views.thesisPolicys),
    path('gradingSystem',views.gradingSystems),
    path('studentFilesPolicy',views.studentFilesPolicys),
    path('requirement',views.requirement),
    path('refundPolicy',views.refundPolicy),
    path('nonDiscriminationPolicy',views.nonDiscriminationPolicys),
    path('educationalOffering/<int:id>',views.education),
    path('gallery',views.gallerys),
    path('contact',views.contact),
    path('contactQuery',views.contactQueryView),
    path('login',views.login),
    path('accreditation',views.accreditation),
    path('describingAccreditation',views.describingAccreditations),
    path('afterGraduationServices',views.afterGraduationServicesFunction),
    path('educationModel',views.educationModels),
    path('advantages/<int:id>',views.advantagesView),
    path('404',views.notFound)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)