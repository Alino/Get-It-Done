from django.db import models
from django.utils import timezone
from tastypie.utils.timezone import now



# Create your models here.
class Todo(models.Model):
    subject = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    def __unicode__(self):
        return self.subject
    def created_today(self):
        return self.date_created.date() == timezone.now().date()
    def save(self, *args, **kwargs):
        return super(Todo, self).save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    def __unicode__(self):
        return self.name
    def created_today(self):
        return self.date_created.date() == timezone.now().date()

class TagsTodoAssoc(models.Model):
    tag_id = models.ForeignKey(Tag)
    todo_id = models.ForeignKey(Todo)

