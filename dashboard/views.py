from sqlite3 import Time
from urllib.request import Request
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Illness, Medicine, Times, NotificationPerson
from django.http import HttpResponse
from .models import Illness, Medicine, Times, NotificationPerson
from .helpers import send_telegram_message
# Create your views here.

def index(request):
    return render(request, "dashboard.html")

def medicine(request):
    return render(request, "medicine.html")

def medicine_add(request):
    if request.method == "POST":
        name = request.POST.get("medicine_name")
        desc = request.POST.get("medicine_desc")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        illness_id = int(request.POST.get("illness"))
        med = Medicine.objects.create(name=name, desc=desc, illness_id=illness_id, start_date=start_date, end_date=end_date)
        return redirect("illness_list")
    illness = Illness.objects.all()
    context = {"illness": illness}
    return render(request, "medicine_add.html", context=context)

def illnes_list(request):
    illnesses = Illness.objects.all().order_by('-id')
    context = {"illnesses": illnesses}
    return render(request, "illness.html", context=context)

def illness_add(request):
    if request.method == "POST":
        name = request.POST.get("illnes_name")
        illnes_desc = request.POST.get("illnes_desc")
        illnes_date = request.POST.get("illnes_date")
        illnes_identified = request.POST.get("illnes_identified")
        user = request.user
        illness  = Illness.objects.create(name=name, desc=illnes_desc, identified_time=illnes_date, identified_by=illnes_identified, user_id=1)
        return redirect("illness_list")
    return render(request, "illness_add.html")


def illness_info(request, pk):
    
    if request.method == "GET":
        illness = Illness.objects.get(id=pk)
        medicine = Medicine.objects.filter(illness=illness)
        context = {"illness": illness, "medicine":medicine}
        return render(request, "illness_info.html", context=context)
    

def illness_edit(request, pk):
    
    if request.method == "POST":
        
        name = request.POST.get("illnes_name")
        illnes_desc = request.POST.get("illnes_desc")
        illnes_date = request.POST.get("illnes_date")
        illnes_identified = request.POST.get("illnes_identified")
        
        
        illness = Illness.objects.get(id=pk)
        
        
        illness.name = name
        illness.desc = illnes_desc
        illness.identified_time = illnes_date
        illness.identified_by = illnes_identified
        illness.save()
        return redirect("illness_list")
        
        
    if request.method == "GET":
        illness = Illness.objects.get(id=pk)
        context = {"illness": illness}
        return render(request, "illness_edit.html", context=context)
    
    
def illness_delete(request, pk):
    if request.method == "POST":
        illness = Illness.objects.get(id=pk)
        illness.delete()
        return redirect("illness_list")
    if request.method == "GET":
        illness = Illness.objects.get(id=pk)
        context = {"illness": illness}
        return render(request, "illness_delete.html", context=context)

        
        
def times_list(request):
        
    times = Times.objects.all()
    
    context = {"times": times}
    
    return render(request, "times.html", context=context)

def time_add(request):
    
    if request.method == "POST":
        time = request.POST.get("time_alert")
        medicine_id = int(request.POST.get("medicine_id"))
        t = Times.objects.create(alert=time, medicine_id=medicine_id)
        return redirect("times_list")

    medicines = Medicine.objects.all()
    context = {"medicines":medicines}

    return render(request, "time_add.html", context=context)


def notification(request):
    db = NotificationPerson.objects.all()
    context = {'db':db}
    return render(request, "notification.html", context=context)




def notification_add(request):
    if request.method == 'POST':
        person = request.POST.get("person_add")
        telegram_id = request.POST.get("telegram")
        name = request.POST.get("first_name")
        person_2 = request.POST.get("person_add_2")
        telegram_id_2 = request.POST.get("telegram_2")
        name_2 = request.POST.get("first_name_2")
        NotificationPerson.objects.create(who=person, telegram_id=telegram_id, first_name=name, who_2=person_2, telegram_id_2=telegram_id_2, first_name_2=name_2 )
        return HttpResponseRedirect("notification/")

    db = NotificationPerson.objects.all()
    context = {'db':db}
    return render(request, "notification_add.html", context)

def notification_info(request, pk):
    not_all = NotificationPerson.objects.all()
    if request.method == "GET":
        notification = NotificationPerson.objects.get(id=pk)
        context = {"db": notification, 'xb':not_all }
    
        return render(request, "notification_info.html", context=context)

def notification_edit(request, pk):
    notification = NotificationPerson.objects.get(id=pk)
    context = {"notification": notification}
    if request.method == "POST":
        
        who = request.POST.get("notification_who")
        telegram = request.POST.get("telegram_id")
        name = request.POST.get("first_name")
        who_2 = request.POST.get("notification_who_2")
        telegram_2 = request.POST.get("telegram_id_2")
        name_2 = request.POST.get("first_name_2")


    
        
        notification = NotificationPerson.objects.get(id=pk)
        
        
        notification.name = who
        notification.telegram_id = telegram
        notification.first_name = name
        notification.name_2 = who_2
        notification.telegram_id_2 = telegram_2
        notification.first_name_2 = name_2
        notification.save()
        return redirect("notification_list")
        
    return render(request, "notification_edit.html", context)


def notification_delete(request, pk):
    if request.method == "POST":
        illness = NotificationPerson.objects.get(id=pk)
        illness.delete()
        return redirect("notification_list")
   
    elif request.method == "GET":
        notification = NotificationPerson.objects.get(id=pk)
        context = {"notification": notification}
        return render(request, "notification_delete.html", context=context)
        
    notifications = NotificationPerson.objects.all()
    context = {"notifications": notifications}
    return render(request, "notification.html", context=context)

def notification_add(request):
    if request.method == "POST":
        who = request.POST.get("who")
        first_name = request.POST.get("who")
        telegram_id = request.POST.get("telegram_id")
        who_2 = request.POST.get("who_2")
        first_name_2 = request.POST.get("who_2")
        telegram_id_2 = request.POST.get("telegram_id_2")
        noti = NotificationPerson.objects.create(who=who, telegram_id=telegram_id, first_name=first_name,who_2=who_2, telegram_id_2=telegram_id_2, first_name_2=first_name_2, user_id=1)
        return redirect("notification_list")
    
    
    return render(request, "notification_add.html")