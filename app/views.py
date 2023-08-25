from django.shortcuts import render
from app.models import *
# Create your views here.


# This 3 function is created to display all the saved data.

# This function is created for storing Topic Objects.
def display_topic(request):
    QSTO= Topic.objects.all()
    d= {'QSTO' : QSTO}
    return render(request, 'display_topic.html', context= d)


# This function is created for storing Webpage Objects.
def display_webpage(request):
    QSWO = Webpage.objects.all()
    d= {'QSWO' : QSWO}
    return render(request, 'display_webpage.html', context= d)


# This function is created for storing AccessRecord Object
def display_access(request):
    QSAO = AccessRecord.objects.all()
    d = {'QSAO' : QSAO }
    return render(request, 'display_access.html', context= d)




# This 3 function is created to insert data in them.

# This function is created to add data in Topic.
def insert_topic(request):
    topic=input('enter topic_name: ')
    TO=Topic.objects.get_or_create(topic_name=topic)[0]
    TO.save()

    QSTO= Topic.objects.all()
    d={'QSTO': QSTO}
    return render(request,'display_topics.html',context= d)




# This function is created to add data in webpage.
def insert_webpage(request):
    tn=input('enter topic_name: ')
    na=input('enter name: ')
    ur=input('enter url: ')

    TO=Topic.objects.get(topic_name=tn)

    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    WO.save()

    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpages.html',d)



# This function is created to add data in accesspage.
def insert_access(request):
    nm= input('Enter your access record name: ')
    dt= input('Enter your date: ')
    ao= input('Enter your author name: ')
    em= input('Enter your email: ')

    nme= Webpage.objects.get(name=nm)

    acc= AccessRecord.objects.get_or_create(name=nme, date= dt, author= ao, email= em)[0]
    acc.save()

    QSAO= AccessRecord.objects.all()
    d= {'QSAO': QSAO}
    return render(request, 'display_access.html', context= d)