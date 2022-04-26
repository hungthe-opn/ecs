from django.db import models
from apps.employees.models import Employees
from apps.lend.models import Lend
from apps.repository.models import Repository


class Manage(models.Model):
    manage_id = models.AutoField(db_column='MANAGE_ID', primary_key=True)  # Field name made lowercase.
    goods_receipt = models.CharField(db_column='GOODS_RECEIPT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    import_date = models.DateField(db_column='IMPORT_DATE', blank=True, null=True)  # Field name made lowercase.
    export = models.CharField(db_column='EXPORT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    export_date = models.DateField(db_column='EXPORT_DATE', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='QUANTITY')  # Field name made lowercase.
    reason = models.CharField(db_column='REASON', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS')  # Field name made lowercase.
    status_manage = models.CharField(db_column='STATUS_MANAGE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lend = models.ForeignKey(Lend, related_name='lend', on_delete=models.CASCADE, db_column='LEND_ID')  # Field name made lowercase.
    id = models.ForeignKey(Employees, models.DO_NOTHING, db_column='ID')  # Field name made lowercase.
    product = models.ForeignKey(Repository, models.DO_NOTHING, db_column='PRODUCT_ID')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manage'