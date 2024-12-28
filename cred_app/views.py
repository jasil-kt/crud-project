from django.shortcuts import render, redirect

from cred_app.forms import TodoForm
from cred_app.models import Todo


# Create your views here.
def landing(request):
    return render(request,'landing.html')


def index(request):

    form = TodoForm()
    if request.method == 'POST':
        form1 = TodoForm(request.POST)
        if form1.is_valid():
            form1.save()
    return render(request,'index.html',{"form":form})


def read(request):
    data = Todo.objects.all()

    return render(request,"read.html",{"data":data})


#delete
def delete_data(request,id):
    data = Todo.objects.get(id=id)
    print(data)
    data.delete()
    return redirect("read")

    return render(request,"read.html")

def update_data(request,id):
    data = Todo.objects.get(id=id)
    form1=TodoForm(instance=data)
    if request.method == 'POST':
        data = TodoForm(request.POST,instance=data)
        if data.is_valid():
            data.save()
        return redirect("read")

    return render(request,"update.html",{"form1":form1})