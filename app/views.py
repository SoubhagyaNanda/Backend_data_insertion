from django.shortcuts import render
from app.models import *
from django.http import*
from django.db.models.functions import Length
from django.db.models import Q
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

# it will show only cricket details.
    QSWO= Webpage.objects.filter(topic_name='cricket')

# it will show all details except cricket
    QSWO= Webpage.objects.exclude(topic_name='cricket')

# it will skip 1st given value and show until the 2nd value
    QSWO = Webpage.objects.all()[1:5:2]

# if we dont give step value it will take until last column.
    QSWO = Webpage.objects.all()[5:6:]

    QSWO = Webpage.objects.all().order_by('name')

    QSWO=Webpage.objects.filter(topic_name='Cricket').order_by('name')

    QSWO=Webpage.objects.all().order_by('-name')

# it will arrenge ascending order
    QSWO=Webpage.objects.all().order_by(Length('name'))

# it will arrenge in descending order
    QSWO=Webpage.objects.all().order_by(Length('name').desc())

# it will check whose name start with V
    QSWO=Webpage.objects.filter(name__startswith='v')

    QSWO=Webpage.objects.all()

# it will check whose url ends with in
    QSWO=Webpage.objects.filter(url__endswith='in')

# it will search specified character is present inside the string or not
    QSWO=Webpage.objects.filter(url__contains='R')

# it will search and return those string who dont have specified character inside string
    QSWO=Webpage.objects.exclude(url__contains='R')

# Writing query sets.
    QSWO=Webpage.objects.filter(Q(topic_name='cricket') & Q(url__contains='in'))

# We can't connect forigen key with same forign key.
    # QSWO=Webpage.objects.filter(Q(topic_name__startswith='f') & Q(topic_name__endswith='l'))

    QSWO=Webpage.objects.exclude(Q(topic_name='football') | Q(url__endswith='in'))

    QSWO= Webpage.objects.all()

    d= {'QSWO' : QSWO}
    return render(request, 'display_webpage.html', context= d)


# This function is created for storing AccessRecord Object
def display_access(request):
    QSAO = AccessRecord.objects.all()
    d = {'QSAO' : QSAO }
    return render(request, 'display_access.html', context= d)





# This Three Function Is Created For Inserting Data
def Insert_Topic(request):
    tn = input('Enter topic_name :')
    to = Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('Data is Inserted Broooooo')



def Insert_Webpage(request):

    tn = input('Enter topic_name :')
    to = Topic.objects.get(topic_name=tn)

    n=input('Enter name :')
    u=input('Enter Url :')
    wo = Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()

    return HttpResponse('Data is Inserted Broooooo')



def Insert_AccessRecord(request):
    tn = input('Enter topic_name :')
    to = Topic.objects.get(topic_name=tn)

    n=input('Enter name :')
    u=input('Enter Url :')
    wo = Webpage.objects.get(topic_name=to,name=n,url=u)

    d = input('Enter date :')
    a = input('Enter author :')
    e = input('Enter email :')
    ao = AccessRecord.objects.get_or_create(name=wo,date=d,author=a,email=e)[0]
    ao.save()

    return HttpResponse('Data is Inserted Broooooo')




def Update_webpage(request):

        QSWO = Webpage.objects.all()

        # Webpage.objects.filter(topic_name='cricket').update(name='VIRAT KOHLI')

        # Webpage.objects.filter(name='VIRAT KOHLI').update(url='https://kohli.com')

        # Webpage.objects.filter(name='Python').update(url='https://kohli.com')

        # Webpage.objects.filter(name='VIRAT KOHLI').update(topic_name='football')

        # Webpage.objects.filter(name='VIRAT KOHLI').update(topic_name='cricket')


        # Webpage.objects.filter(name='VIRAT KOHLI').update(topic_name='Boxing')


        # Webpage.objects.update_or_create(topic_name='kabbadi',defaults={'name':'Messi'})
        # Webpage.objects.all()
        # Webpage.objects.update_or_create(topic_name='Volley Ball',defaults={'name':'NeyMar'})
    
        # RO=Topic.objects.get(topic_name='football')
        # Webpage.objects.update_or_create(name='dileep',defaults={'topic_name':RO, 'url':'http://dileep.com'})
    
        # Webpage.objects.update_or_create(name='Hardhik',defaults={'url':'https://Hardhik.com'})
        # CTO=Topic.objects.get(topic_name='cricket')
        # Webpage.objects.update_or_create(name='Hardhik',defaults={'topic_name':CTO,'url':'https://Hardhik.com'})


        ww= Topic.objects.get(topic_name='WWE')
        Webpage.objects.update_or_create(topic_name=ww, name='HHH', defaults={'url':'http://wwe.in'})

        d = {'QSWO':QSWO}
        return render(request, 'display_webpage.html', context= d)



def Delete_webpage(request):
     
     QSWO = Webpage.objects.all()


     Webpage.objects.filter(name='Hardhik').delete()

     Webpage.objects.filter(topic_name='golf').delete()

     Webpage.objects.filter(topic_name='cricket').delete()

     Webpage.objects.all().delete()
     d = {'QSWO' : QSWO}
     return render(request, 'display_webpage.html', context= d)