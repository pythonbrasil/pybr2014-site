# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Track.description_en_us'
        db.delete_column('schedule_track', 'description_en_us')

        # Deleting field 'Track.name_en_us'
        db.delete_column('schedule_track', 'name_en_us')

        # Adding field 'Track.name_en'
        db.add_column('schedule_track', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Track.description_en'
        db.add_column('schedule_track', 'description_en', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True), keep_default=False)

        # Changing field 'Track.description_pt_br'
        db.alter_column('schedule_track', 'description_pt_br', self.gf('django.db.models.fields.CharField')(default='', max_length=2000))

        # Changing field 'Track.name_pt_br'
        db.alter_column('schedule_track', 'name_pt_br', self.gf('django.db.models.fields.CharField')(default='', max_length=255))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Track.description_en_us'
        raise RuntimeError("Cannot reverse this migration. 'Track.description_en_us' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Track.name_en_us'
        raise RuntimeError("Cannot reverse this migration. 'Track.name_en_us' and its values cannot be restored.")

        # Deleting field 'Track.name_en'
        db.delete_column('schedule_track', 'name_en')

        # Deleting field 'Track.description_en'
        db.delete_column('schedule_track', 'description_en')

        # Changing field 'Track.description_pt_br'
        db.alter_column('schedule_track', 'description_pt_br', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True))

        # Changing field 'Track.name_pt_br'
        db.alter_column('schedule_track', 'name_pt_br', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 11, 9, 41, 54, 791338)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 11, 9, 41, 54, 791216)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'schedule.proposalvote': {
            'Meta': {'object_name': 'ProposalVote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.Session']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'vote': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'schedule.session': {
            'Meta': {'object_name': 'Session'},
            'audience_level': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'proposed'", 'max_length': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.Track']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'schedule.track': {
            'Meta': {'object_name': 'Track'},
            'description_en': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'description_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['schedule']
