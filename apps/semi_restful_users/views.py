from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import User

def index(request):
    context = {
        "users" : User.objects.all()
    }
    return render(request,'semi_restful_users/index.html', context)

def new(request):
    return render(request, "semi_restful_users/new.html")

def edit(request, curr_id):
    context = {
        "user": User.objects.get(id=curr_id)
    }
    return render(request, "semi_restful_users/edit.html", context)

def show(request, curr_id):
    context = {
        "user": User.objects.get(id=curr_id)
    }
    return render(request, "semi_restful_users/show.html", context)

def create(request):
    errors = User.objects.validate(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/new')
    else:
        user = User.objects.create()
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        id = str(user.id)
        return redirect("/users/" + id)

def destroy(request, curr_id):
    user = User.objects.get(id=curr_id)
    user.delete()
    return redirect("/users")

def update(request, curr_id):
    errors = User.objects.validate(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/' + curr_id + '/edit/')
    else:
        user = User.objects.get(id=curr_id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        id = str(user.id)
    return redirect("/users/" + id)