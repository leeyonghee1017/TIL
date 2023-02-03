from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .form import PhotoForm

# Create your views here.
def photo_list(request):
    photo = Photo.objects.all()

    return render(request,'photo_list.html',{'photos':photo})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo,pk=pk)
    return render(request,'photo_detail.html',{'photo':photo})

def photo_post(request):
    if request.method == "GET":
        return render(request,'photo_post.html')
    else :
        title = request.POST['title']
        autho = request.POST['autho']
        image = request.POST['image']
        decription = request.POST['decription']
        price = request.POST['price']

        result = Photo.objects.create(title=title,autho=autho,image=image,decription=decription,price=price)

        if result:
            return redirect('photo_list')
        else:
            return redirect('photo_post')

def photo_edit(request,pk):
    photo = get_object_or_404(Photo,pk=pk)

    if request.method=="GET":
        form=PhotoForm(instance=photo)
        return render(request,'photo_edit.html',{'form':form})
    else :
        form=PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo=form.save(commit=False)
            photo.save()
            return redirect('photo_detail',pk=photo.id)

    