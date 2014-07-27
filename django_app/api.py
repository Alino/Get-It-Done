from tastypie.resources import ModelResource
from django_app.models import Todo

class TodoResource(ModelResource):
    class Meta:
        queryset = Todo.objects.all()
        resource_name = 'todo'
        fields = ['subject', 'finished']

class TagResource(ModelResource):
    class Meta:
        queryset = Todo.objects.all()
        resource_name = 'tag'