from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'
        ordering = ['name']

    def __str__(self):
        return '%d: %s' % (self.category_id, self.name)
