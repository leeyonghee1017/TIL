from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.paginator import Paginator

# Create your views here.
def todo_list(request):
    todo = Todo.objects.filter(complete=False)
    paginator = Paginator(todo,5)
    page_num = request.GET.get('page','1')
    page_obj = paginator.get_page(page_num)
    return render(request,'todo/todo_list.html',{'todo':page_obj})

def todo_post(request):
    if request.method == 'GET':
        form = TodoForm()
        return render(request,'todo/todo_post.html',{'form':form})
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            
            upload_file = request.FILES['imagefile']
            upload = default_storage.save(upload_file.name,ContentFile(upload_file.read()))
            
            Todo.objects.filter(id=todo.id).update(imagefile=upload_file)

            return redirect('todo:todo_list')

def todo_detail(request,pk):
    todo = Todo.objects.get(id=pk)
    return render(request,'todo/todo_detail.html',{'todo':todo})

def todo_edit(request,pk):
    todo=Todo.objects.get(id=pk)
    if request.method=="GET":
        form = TodoForm(instance=todo)
        return render(request,'todo/todo_post.html',{'form':form})
    else:
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()

            upload_file = request.FILES['imagefile']
            upload = default_storage.save(upload_file.name,ContentFile(upload_file.read()))

            Todo.objects.filter(id=todo.id).update(imagefile=upload_file)

            return redirect('todo:todo_list')

def done_list(request):
    todo = Todo.objects.filter(complete=True)
    return render(request,'todo/done_list.html',{'todo':todo})

def todo_done(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo:todo_list')

def todo_delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todo:todo_list')