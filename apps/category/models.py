from django.db import models


class Category(models.Model):
    category_id = models.CharField(db_column='CATEGORY_ID', primary_key=True, max_length=4)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'
        # unique_together = ['category_id, name']
        ordering = ['name']

    def __str__(self):
        return '%d: %s' % (self.category_id, self.name)
