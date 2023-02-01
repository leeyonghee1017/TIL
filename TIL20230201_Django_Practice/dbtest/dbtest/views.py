from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Myboard

def index(request):
    myboard_all = Myboard.objects.all()
    print(myboard_all)
    return render(request,'index.html',{'list':myboard_all})

def detail(request,id):    
    return render(request,'detail.html',{'dto':Myboard.objects.get(id=id)})

def update_form(request,id):
    return render(request,'update.html',{'dto':Myboard.objects.get(id=id)})

def update_proc(request):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    myboard = Myboard.objects.filter(id=id)
    result_title = myboard.update(mytitle=mytitle)
    result_content = myboard.update(mycontent=mycontent)

    if result_title + result_content == 2:
        return redirect('/detail/'+id)
    else:
        return redirect('/update_form/'+id)

def insert_form(request):
    return render(request, 'insert.html')

def insert_proc(request):
    myname=request.POST['myname']
    mytitle=request.POST['mytitle']
    mycontent=request.POST['mycontent']
    
    result = Myboard.objects.create(myname=myname,mytitle=mytitle,mycontent=mycontent,mydate=timezone.now())
    if result:
        return redirect('index')
    else:
        return redirect('insertform')

def delete_proc(request, id):   
    result = Myboard.objects.filter(id=id).delete()   
    if result[0]:
        return redirect('index')
    else:
        return redirect('/detail/'+id)