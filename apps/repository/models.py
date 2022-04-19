from django.db import models

from apps.type.models import Type


class Repository(models.Model):
    FLOORS = (
                (11, 'Tang 11'),
                (13, 'Tang 13'),
                (13.1, 'Tang 13 CRM'),
                (15, 'Tang 15'),
                (17, 'Tang 17')
            )
    product_id = models.CharField(db_column='PRODUCT_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=30)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='QUANTITY', blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lend_device = models.IntegerField(db_column='LEND_DEVICE')  # Field name made lowercase.
    sum_device = models.IntegerField(db_column='SUM_DEVICE')  # Field name made lowercase.
    residual = models.IntegerField(db_column='RESIDUAL')  # Field name made lowercase.
    floor = models.IntegerField(db_column='FLOOR', choices=FLOORS, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.ForeignKey(Type,related_name="repository", on_delete=models.CASCADE, db_column='TYPE_ID', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repository'
