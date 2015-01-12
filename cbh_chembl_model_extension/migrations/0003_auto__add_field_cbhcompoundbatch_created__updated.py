# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CBHCompoundBatch.related_molregno'
        db.add_column(u'cbh_chembl_model_extension_cbhcompoundbatch', 'created', self.gf('django.db.models.fields.DateTimeField')(null=True))
        db.add_column(u'cbh_chembl_model_extension_cbhcompoundbatch', 'modified', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'CBHCompoundBatch.related_molregno'
        db.delete_column(u'cbh_chembl_model_extension_cbhcompoundbatch', 'created')
        db.delete_column(u'cbh_chembl_model_extension_cbhcompoundbatch', 'modified')

    models = {
        u'cbh_chembl_model_extension.cbhcompoundbatch': {
            'Meta': {'object_name': 'CBHCompoundBatch'},
            'ctab': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'custom_fields': (u'django_hstore.fields.DictionaryField', [], {}),
            'editable_by': (u'django_hstore.fields.DictionaryField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'related_molregno_id': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'null': 'True', 'blank': 'True'}),
            'warnings': (u'django_hstore.fields.DictionaryField', [], {}),
            'viewable_by': (u'django_hstore.fields.DictionaryField', [], {})
        }
    }

    complete_apps = ['cbh_chembl_model_extension']