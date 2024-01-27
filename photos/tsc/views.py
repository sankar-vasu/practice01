from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import tsc_stores,photo_upload,brand_names
from django.contrib import messages
from datetime import datetime
from django.db.models import Sum , Avg , Count
from .forms import Person_datails_form
# Create your views here.
#test

def display(request):
    POST = tsc_stores.objects.all()
    return render(request,"display.html",{"POST":POST})

# store details entry

def store_entry(request):
    if request.method == "POST":
        n = request.POST['store_name']
        c = request.POST['store_code']
        d = request.POST['store_createdate']
        k = tsc_stores(store_name=n,store_code=c,store_createdate=d)
        k.save()
        messages.success(request,"Record was added")
    return render(request,"store_entry.html")

#Delete store name

def del_store(request,id):
    if request.method=="POST":
        d=tsc_stores.objects.get(id=id)
        d.delete()
    return redirect("/")

#store name edit
def store_edit(request,id):
    if request.method=="POST":
        data = tsc_stores.objects.get(id=id)
        context={
            "data":data
        }
    return render(request,"store_edit.html",context)


#save store edit data
def save_store_edit(request,id):
    if request.method == "POST":
        n = request.POST['store_name']
        c = request.POST['store_code']
        d = request.POST['store_createdate']
        k = tsc_stores.objects.get(id=id)
        k.store_name = n
        k.store_code=c
        if d is None:
            date = k.store_createdate
        else:
            date = d
        k.store_createdate = date
        k.save()
        messages.success(request,"Successfully updated")

    return HttpResponseRedirect('/')


# store photos upload

def photos_upload(request):
    if request.method=="POST":
        n = request.POST['store_name']
        b = request.POST['brand_name']
        p = request.FILES.get('photo')
        #d = request.POST['date']
        k = photo_upload(store_name=n,photo=p,brand_name=b)
        k.save()
    stores = tsc_stores.objects.all()
    brands = brand_names.objects.all()
    context ={
            "store":stores,
            "brands":brands,
        }
    return render(request,"photos_upload.html",context)

#photos display
def photos_display(request):
    POST = photo_upload.objects.all().order_by('date')
    return render(request,"photos_display.html",{"POST":POST})

#brand name entry
def brand_name_entry(request):
    if request.method=="POST":
        bn = request.POST['brand_name']
        k = brand_names(brand_Name=bn)
        k.save()
    POST = brand_names.objects.all()
    return render(request,"brand_names.html",{"POST":POST})

#filter data
def filter_data(request):

    #if request.method=="POST":
    sn = request.GET.get('store_name')
    bn = request.GET.get('brand_name')
    fd = request.GET.get('fromdate')
    td = request.GET.get('todate')
    if sn and bn and fd and td :
        sc = photo_upload.objects.filter(store_name=sn, brand_name=bn,date__range=[fd,td]).all()
    elif sn and fd and td :
        sc = photo_upload.objects.filter(store_name=sn,date__range=[fd, td]).all()
    elif bn and fd and td :
        sc = photo_upload.objects.filter(brand_name=bn,date__range=[fd, td]).all()
    elif sn and bn:
        sc = photo_upload.objects.filter(store_name=sn, brand_name=bn).all()


    elif sn:
        sc = photo_upload.objects.filter(store_name=sn).all()
    elif bn:
        sc = photo_upload.objects.filter(brand_name=bn).all()
    elif fd and td:
        sc = photo_upload.objects.filter(date__range=[fd, td]).all()

    else:
        sc = photo_upload.objects.all().order_by('date')

    n = sc.count()
    store_count = sc.values('store_name').annotate(total=Count('store_name'))
    brand_count = sc.values('brand_name').annotate(total=Count('brand_name'))

    #sc = photo_upload.objects.filter(date__range=[fd,td],store_name=sn)
    #sc = photo_upload.objects.filter(store_name=sn,brand_name=br).values()
    data = tsc_stores.objects.all()
    data2 = brand_names.objects.all()

    context = {
        "data":data,
        "search":sc,
        "data2":data2,
        "count":n,
        "st":store_count,
        "bn":brand_count,

    }
    return render(request, "search.html",context)

#Main Index page
def main_page(request):
    form = Person_datails_form()
    if request.method=="POST":
        form = Person_datails_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record was added")

    else:
        form = Person_datails_form()
    context = {
        "form": form,
    }
    return render(request,"index.html",context)
    #return redirect("index.html",context)


