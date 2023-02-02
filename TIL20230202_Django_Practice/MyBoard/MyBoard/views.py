from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import MyBoard

def index(request):
    myboard_all_search = MyBoard.objects.all().order_by('-id')

    paginator = Paginator(myboard_all_search,5)
    page_num = request.GET.get('page','1')

    page_obj = paginator.get_page(page_num)

    print('----------------count----------------')
    print(page_obj.count)
    print('----------------number----------------')
    print(page_obj.number)
    print('----------------num_pages----------------')
    print(page_obj.paginator.num_pages)
    print('----------------range----------------')
    print(page_obj.paginator.page_range)
    print('----------------previous, next----------------')
    print(page_obj.has_previous())
    print(page_obj.has_next())
    try:
        print('----------------previous error----------------')
        print(page_obj.previous_page_number())
        print('----------------next error----------------')
        print(page_obj.next_page_number())
    except:
        pass
    print('----------------start_index----------------')
    print(page_obj.start_index())
    print('----------------end_index----------------')
    print(page_obj.end_index())
    

    #return render(request,'index.html',{'myboard_list':myboard_all_search})
    return render(request,'index.html',{'myboard_list':page_obj})

def insert_form(request):
    return render(request,'insert_form.html')

def insert_proc(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    result = MyBoard.objects.create(myname=myname,mytitle=mytitle,mycontent=mycontent,mydate=timezone.now())

    if result:
        return redirect('index')
    else:
        return redirect('insertform')

def detail(request, id):    
   return render(request,'detail.html',{'dto':MyBoard.objects.get(id=id)})

def delete_proc(request,id):
    result = MyBoard.objects.filter(id=id).delete()
    if result[0]:
        return redirect('index')
    else:
        return redirect('/detail/'+id)

def update_form(request,id):
    return render(request,'update_form.html',{'dto':MyBoard.objects.get(id=id)})

def update_proc(request):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    myboard = MyBoard.objects.filter(id=id)
    result_title = myboard.update(mytitle=mytitle)
    result_content = myboard.update(mycontent=mycontent)

    if result_title + result_content == 2:
        return redirect('/detail/'+id)
    else:
        return redirect('/updateform/'+id)