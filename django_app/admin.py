from django.contrib import admin
from django_app.models import Todo, Tag, TagsTodoAssoc

# Register your models here.
admin.site.register(Todo)
admin.site.register(Tag)
admin.site.register(TagsTodoAssoc)
