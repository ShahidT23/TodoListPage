from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import TodoItem
from django.http.response import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def homepage(request):
    all_todo = TodoItem.objects.all()
    return render(request, 'homepage.html',{"all_todo":all_todo})

@require_http_methods(["POST"])
def add_todo(request):
    todo_text = request.POST["tododata"]
    obj =TodoItem(description=todo_text)
    obj.save()
    return HttpResponseRedirect(reverse('app:homepage'))

@require_http_methods(["GET"])
def delete_todo(request ,id):
    TodoItem.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('app:homepage'))


@require_http_methods(["GET"])
def update_todo(request,id):
    obj = TodoItem.objects.get(id=id)
    obj.current_status = not(obj.current_status)
    obj.save()
    return HttpResponseRedirect(reverse('app:homepage'))