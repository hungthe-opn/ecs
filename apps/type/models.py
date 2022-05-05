from django.db import models
from apps.category.models import Category


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type'
