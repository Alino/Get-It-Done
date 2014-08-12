from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    owner = models.ForeignKey(User)
    description = models.CharField(max_length=50)
    done = models.BooleanField()
    updated = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=20)
    updated = models.DateTimeField()

class TagsTodoAssoc(models.Model):
    owner = models.ForeignKey(User)
    tag_id = models.ForeignKey(Tag)
    todo_id = models.ForeignKey(Todo)