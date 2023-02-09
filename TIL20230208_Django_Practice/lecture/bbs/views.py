from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Comment
from .forms import BoardForm, BoardDetailForm
from django.http import JsonResponse
# Create your views here.
def b_list(request):
    
    if request.user.is_authenticated:
        posts = Board.objects.all().order_by('-id')
        return render(request,'bbs/list.html',{'posts':posts})
    else:
        return redirect('home')

def b_create(request):
    if request.method == "GET":
        board_form = BoardForm()        
    else : 
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board_form.save()
            return redirect('bbs:b_list')
    return render(request,'bbs/create.html',{'board_form':board_form})    

def b_detail(request,board_id):
    post = get_object_or_404(Board,id=board_id)
    board_detail_form = BoardDetailForm(instance=post)
    board_detail_form.show_board_detail()

    return render(request,'bbs/detail.html',{'board_detail_form':board_detail_form})

def b_update(request,board_id):
    post = get_object_or_404(Board,id=board_id)
    board_detail_form = BoardDetailForm(instance=post)
    board_detail_form.show_board_update()

    return render(request,'bbs/update.html',{'board_detail_form':board_detail_form})

def b_update_process(request,board_id):
    post = get_object_or_404(Board,id=board_id)
    if request.method=="POST":
        board_detail_form = BoardDetailForm(request.POST,instance=post)

        if board_detail_form.is_valid():
            board_detail_form.save()
            board_detail_form.show_board_detail()
            return render(request,'bbs/detail.html',{'board_detail_form':board_detail_form})
    
    return redirect('home')

def b_like(request,board_id):
    post = get_object_or_404(Board,id=board_id)
    post.b_like_count+=1
    post.save()

    board_detail_form = BoardDetailForm(instance=post)
    board_detail_form.show_board_detail()

    return render(request,'bbs/detail.html',{'board_detail_form':board_detail_form})  

def b_delete(request,board_id):
    post = get_object_or_404(Board,id=board_id) 
    post.delete()
    return redirect('bbs:b_list')

def c_create(request,board_id):
    comment = Comment()
    comment.c_author = request.GET['user_name']
    comment.c_content = request.GET['user_content']
    comment.board_id = request.GET['board_id']
    comment.save()
    
    return JsonResponse({
        'comment_author': request.GET['user_name'],
        'comment_content': request.GET['user_content'],
        'comment_id': request.GET['board_id']
    }, json_dumps_params= { 'ensure_ascii' : True } )