from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import AddData
from django.http import request
from .models import Signup


def addData(request):
    try:
        context = {}
        if request.method == "GET":
            context['form'] = AddData()
            context['data'] = Signup.objects.all()
            return render(request, 'home.html', context)

        if request.method == "POST":
            form = AddData(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/home?=success')
            else:
                return redirect('/home?=failed')
    except Exception as err:
        print("Error in the add data function. Please Check.", err)
        return redirect('/home?=failed')

def updateData(request, id):
    try:
        context = {}
        itemData = get_object_or_404(Signup, id= id)
        if request.method == "POST":
            form = AddData(request.POST, instance=itemData)
            if form.is_valid():
                form.save()
                return redirect('/home?=success')
            else:
                return redirect('/update?=failed')

        if request.method == "GET":
            form = AddData(instance=itemData)
            context['form'] = form
            return render(request, 'update.html', context)

    except Exception as err:
        print("Error in the update function.", err)
        return redirect('/update?=failed')

def deleteData(request, id):
    if request.method == 'GET':
        user = get_object_or_404(Signup, id=id)
        user.delete()
        return redirect('/home?=Success')
