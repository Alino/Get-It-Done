from django.shortcuts import render
from tastypie.utils.timezone import now
from django.http import HttpResponse
from django_app.models import Todo, Tag, TagsTodoAssoc

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    tags = Tag.objects.all()
    response_string = '<br />'.join(["id: %s, subject: %s" % (todo.id, todo.subject) for todo in todos])
    return HttpResponse(response_string)