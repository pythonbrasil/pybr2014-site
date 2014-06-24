# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PromoCode'
        db.create_table('promo_code_promocode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, unique=True, null=True, blank=True)),
            ('sent', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('promo_code', ['PromoCode'])


    def backwards(self, orm):
        
        # Deleting model 'PromoCode'
        db.delete_table('promo_code_promocode')


    models = {
        'promo_code.promocode': {
            'Meta': {'object_name': 'PromoCode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        }
    }

    complete_apps = ['promo_code']
