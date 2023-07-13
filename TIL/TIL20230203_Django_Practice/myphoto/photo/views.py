from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Photo
from .form import PhotoForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


# Create your views here.
def photo_list(request):
    photo = Photo.objects.all()

    return render(request,'photo_list.html',{'photos':photo})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo,pk=pk)
    return render(request,'photo_detail.html',{'photo':photo})

def photo_post(request):
    if request.method == "GET":
        form = PhotoForm()
        return render(request,'photo_post.html',{'form':form})
    else :
        form = PhotoForm(request.POST)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()

            upload_file = request.FILES['imagefile']
            default_storage.save(upload_file.name,ContentFile(upload_file.read()))
            Photo.objects.filter(id=photo.id).update(imagefile=upload_file)
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

def photo_delete(request,pk):
    result = Photo.objects.filter(pk=pk).delete()
    if result[0]:
        return redirect('photo_list')
    else:
        return redirect('photo/'+pk)


    