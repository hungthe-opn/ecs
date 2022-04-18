from django.db import models
from apps.category.models import Category


class Type(models.Model):
    type_id = models.CharField(db_column='TYPE_ID', primary_key=True, max_length=4)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='QUANTITY', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='CATEGORY_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'type'
