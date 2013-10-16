# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'list_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=30)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('byline', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('hyperlink', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'list', ['Article'])

        # Adding M2M table for field impact on 'Article'
        m2m_table_name = db.shorten_name(u'list_article_impact')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm[u'list.article'], null=False)),
            ('impact', models.ForeignKey(orm[u'list.impact'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'impact_id'])

        # Adding M2M table for field training on 'Article'
        m2m_table_name = db.shorten_name(u'list_article_training')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm[u'list.article'], null=False)),
            ('training', models.ForeignKey(orm[u'list.training'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'training_id'])

        # Adding model 'Impact'
        db.create_table(u'list_impact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'list', ['Impact'])

        # Adding model 'Training'
        db.create_table(u'list_training', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=30)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['list.TrainingType'])),
            ('eventnumber', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('lng', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('attendance', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'list', ['Training'])

        # Adding M2M table for field article on 'Training'
        m2m_table_name = db.shorten_name(u'list_training_article')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('training', models.ForeignKey(orm[u'list.training'], null=False)),
            ('article', models.ForeignKey(orm[u'list.article'], null=False))
        ))
        db.create_unique(m2m_table_name, ['training_id', 'article_id'])

        # Adding model 'TrainingType'
        db.create_table(u'list_trainingtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'list', ['TrainingType'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'list_article')

        # Removing M2M table for field impact on 'Article'
        db.delete_table(db.shorten_name(u'list_article_impact'))

        # Removing M2M table for field training on 'Article'
        db.delete_table(db.shorten_name(u'list_article_training'))

        # Deleting model 'Impact'
        db.delete_table(u'list_impact')

        # Deleting model 'Training'
        db.delete_table(u'list_training')

        # Removing M2M table for field article on 'Training'
        db.delete_table(db.shorten_name(u'list_training_article'))

        # Deleting model 'TrainingType'
        db.delete_table(u'list_trainingtype')


    models = {
        u'list.article': {
            'Meta': {'object_name': 'Article'},
            'byline': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'hyperlink': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'impact': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['list.Impact']", 'symmetrical': 'False'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'}),
            'training': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'events+'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['list.Training']"})
        },
        u'list.impact': {
            'Meta': {'object_name': 'Impact'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '20'})
        },
        u'list.training': {
            'Meta': {'object_name': 'Training'},
            'article': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'stories+'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['list.Article']"}),
            'attendance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'eventnumber': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['list.TrainingType']"})
        },
        u'list.trainingtype': {
            'Meta': {'object_name': 'TrainingType'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['list']