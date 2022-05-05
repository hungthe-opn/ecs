from django.db import models
from apps.employees.models import Employees
from apps.lend.models import Lend
from apps.repository.models import Repository


class Manage(models.Model):
    goods_receipt = models.CharField(max_length=45, blank=True, null=True)
    import_date = models.DateField(blank=True, null=True)
    export = models.CharField(max_length=45, blank=True, null=True)
    export_date = models.DateField(blank=True, null=True)
    quantity = models.IntegerField()
    reason = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    status_manage = models.CharField(max_length=45, blank=True, null=True)
    lend = models.ForeignKey(Lend, related_name="manage", on_delete=models.CASCADE)
    employee = models.ForeignKey(Employees, related_name="employee", on_delete=models.CASCADE)
    repository = models.ForeignKey(Repository, related_name="repository", on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True )
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'manage'