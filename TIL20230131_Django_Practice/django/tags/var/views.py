from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'var/index.html')

def variable01(request):
    my_list = ['python','django','template']
    return render(request,'var/variable01.html',{'lst':my_list})

def variable02(request):
    my_dict = {'name':'lee','class':'AI취업'}
    return render(request,'var/variable02.html',{'dict':my_dict})

def testfor(request):
    return render(request,'var/testfor.html',{'number':range(1,11)})

def if01(request):
    return render(request,'var/if01.html',{'user':{'id':'lyh'}})

def if02(request):
    member = {'id':'mulit','class':'ai','role':'manager'}
    return render(request,'var/if02.html',{'member':member})