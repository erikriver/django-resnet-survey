# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Survey'
        db.create_table('survey_survey', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=1024)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('use_cookies', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('survey', ['Survey'])

        # Adding model 'QuestionGroup'
        db.create_table('survey_questiongroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
        ))
        db.send_create_signal('survey', ['QuestionGroup'])

        # Adding model 'Question'
        db.create_table('survey_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.Survey'])),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.QuestionGroup'], null=True, blank=True)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order_number', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('survey', ['Question'])

        # Adding model 'Choice'
        db.create_table('survey_choice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.Question'])),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('survey', ['Choice'])

        # Adding model 'Answer'
        db.create_table('survey_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('choice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.Choice'])),
            ('ballot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.Ballot'], null=True)),
        ))
        db.send_create_signal('survey', ['Answer'])

        # Adding model 'Ballot'
        db.create_table('survey_ballot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.GenericIPAddressField')(default='127.0.0.1', max_length=39)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.Survey'], null=True)),
        ))
        db.send_create_signal('survey', ['Ballot'])


    def backwards(self, orm):
        # Deleting model 'Survey'
        db.delete_table('survey_survey')

        # Deleting model 'QuestionGroup'
        db.delete_table('survey_questiongroup')

        # Deleting model 'Question'
        db.delete_table('survey_question')

        # Deleting model 'Choice'
        db.delete_table('survey_choice')

        # Deleting model 'Answer'
        db.delete_table('survey_answer')

        # Deleting model 'Ballot'
        db.delete_table('survey_ballot')


    models = {
        'survey.answer': {
            'Meta': {'object_name': 'Answer'},
            'ballot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['survey.Ballot']", 'null': 'True'}),
            'choice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['survey.Choice']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'survey.ballot': {
            'Meta': {'object_name': 'Ballot'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'default': "'127.0.0.1'", 'max_length': '39'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['survey.Survey']", 'null': 'True'})
        },
        'survey.choice': {
            'Meta': {'object_name': 'Choice'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['survey.Question']"})
        },
        'survey.question': {
            'Meta': {'ordering': "['order_number']", 'object_name': 'Question'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['survey.QuestionGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'order_number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['survey.Survey']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'survey.questiongroup': {
            'Meta': {'object_name': 'QuestionGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'})
        },
        'survey.survey': {
            'Meta': {'object_name': 'Survey'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '1024'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'use_cookies': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['survey']