from django.shortcuts import render, redirect
from .models import Url
import uuid
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def links(request):
    data = Url.objects.all()
    index =  [i for i in range(len(data))]
    link = [data[i].link for i in range(len(data))]
    uuid = [data[i].uuid for i in range(len(data))]
    stored = {'Values': zip(index, link, uuid)}
    return render(request,'links.html',stored)

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        if request.POST['personal'] != '':
            try:
                if Url.objects.get(uuid=request.POST['personal']).uuid == request.POST['personal']:
                    uid = str(uuid.uuid4())[:5]
            except Url.DoesNotExist:
                uid = request.POST['personal'][:10]
        else:
            uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def delete(request):
    if request.method == 'POST':
        delthis = request.POST['delthis']
        try:
            Url.objects.filter(uuid=delthis).delete()
        except Url.DoesNotExist:
            pass
        return HttpResponse('location.reload();')

def go(request,pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)