# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Todo'
        db.create_table(u'django_app_todo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('finished', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'django_app', ['Todo'])

        # Adding model 'Tag'
        db.create_table(u'django_app_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'django_app', ['Tag'])

        # Adding model 'TagsTodoAssoc'
        db.create_table(u'django_app_tagstodoassoc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_app.Tag'])),
            ('todo_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_app.Todo'])),
        ))
        db.send_create_signal(u'django_app', ['TagsTodoAssoc'])


    def backwards(self, orm):
        # Deleting model 'Todo'
        db.delete_table(u'django_app_todo')

        # Deleting model 'Tag'
        db.delete_table(u'django_app_tag')

        # Deleting model 'TagsTodoAssoc'
        db.delete_table(u'django_app_tagstodoassoc')


    models = {
        u'django_app.tag': {
            'Meta': {'object_name': 'Tag'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'django_app.tagstodoassoc': {
            'Meta': {'object_name': 'TagsTodoAssoc'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_app.Tag']"}),
            'todo_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_app.Todo']"})
        },
        u'django_app.todo': {
            'Meta': {'object_name': 'Todo'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['django_app']