# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Category(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'category'

#
# class Departments(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     code = models.CharField(unique=True, max_length=32)
#     parent_code = models.CharField(max_length=64, blank=True, null=True)
#     company_code = models.CharField(max_length=64, blank=True, null=True)
#     postal_code = models.CharField(max_length=10, blank=True, null=True)
#     name = models.CharField(max_length=64)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     color_code = models.CharField(max_length=10, blank=True, null=True)
#     created_by = models.CharField(max_length=4)
#     updated_by = models.CharField(max_length=4)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     employee_id = models.CharField(max_length=4, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'departments'


# class Employees(models.Model):
#     id = models.CharField(primary_key=True, max_length=4)
#     position_id = models.IntegerField()
#     department_code = models.CharField(max_length=32, blank=True, null=True)
#     account_id = models.IntegerField()
#     job_title_code = models.CharField(max_length=32)
#     company_code = models.CharField(max_length=32)
#     name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=20, blank=True, null=True)
#     phone_family = models.CharField(max_length=20, blank=True, null=True)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     current_address = models.CharField(max_length=255, blank=True, null=True)
#     gender = models.IntegerField(blank=True, null=True)
#     birthday = models.DateField(blank=True, null=True)
#     other_email = models.CharField(max_length=255, blank=True, null=True)
#     identity_number = models.CharField(max_length=20, blank=True, null=True)
#     identity_card_date = models.DateField(blank=True, null=True)
#     identity_card_place = models.CharField(max_length=255, blank=True, null=True)
#     insurance_number = models.CharField(max_length=20, blank=True, null=True)
#     image_url = models.CharField(max_length=255, blank=True, null=True)
#     number_of_days_leave = models.FloatField()
#     link_facebook = models.CharField(max_length=255, blank=True, null=True)
#     nation = models.CharField(max_length=45, blank=True, null=True)
#     nationality = models.CharField(max_length=45, blank=True, null=True)
#     level = models.IntegerField(blank=True, null=True)
#     japanese_level = models.IntegerField(blank=True, null=True)
#     work_type = models.CharField(max_length=64, blank=True, null=True)
#     visa_card_number = models.CharField(max_length=20, blank=True, null=True)
#     visa_date_period = models.DateField(blank=True, null=True)
#     university_name = models.CharField(max_length=255, blank=True, null=True)
#     type_of_work_time = models.IntegerField(blank=True, null=True)
#     join_date = models.DateField()
#     resignation_date = models.DateField(blank=True, null=True)
#     resignation_reason = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'employees'


# class Lend(models.Model):
#     id = models.IntegerField(primary_key=True)
#     stt = models.IntegerField()
#     device_code = models.CharField(max_length=45)
#     rent_time = models.DateField(blank=True, null=True)
#     pay_time = models.DateField(blank=True, null=True)
#     describe = models.CharField(max_length=255, blank=True, null=True)
#     quantity = models.IntegerField(blank=True, null=True)
#     status = models.CharField(max_length=45, blank=True, null=True)
#     insurance_start = models.DateField(blank=True, null=True)
#     insurance_end = models.DateField(blank=True, null=True)
#     warranty = models.CharField(max_length=30, blank=True, null=True)
#     condition = models.CharField(max_length=45, blank=True, null=True)
#     employee = models.ForeignKey(Employees, models.DO_NOTHING)
#     repository = models.ForeignKey('Repository', models.DO_NOTHING)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'lend'


# class Manage(models.Model):
#     goods_receipt = models.CharField(max_length=45, blank=True, null=True)
#     import_date = models.DateField(blank=True, null=True)
#     export = models.CharField(max_length=45, blank=True, null=True)
#     export_date = models.DateField(blank=True, null=True)
#     quantity = models.IntegerField()
#     reason = models.CharField(max_length=255, blank=True, null=True)
#     status = models.IntegerField()
#     status_manage = models.CharField(max_length=45, blank=True, null=True)
#     lend = models.ForeignKey(Lend, models.DO_NOTHING)
#     employee = models.ForeignKey(Employees, models.DO_NOTHING)
#     repositoy = models.ForeignKey('Repository', models.DO_NOTHING)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'manage'


# class Repository(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=30)
#     quantity = models.IntegerField(blank=True, null=True)
#     color = models.CharField(max_length=45, blank=True, null=True)
#     lend_device = models.IntegerField()
#     sum_device = models.IntegerField()
#     residual = models.IntegerField()
#     floor = models.IntegerField(blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     type = models.ForeignKey('Type', related_name="type_id", on_delete=models.CASCADE, blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'repository'


# class Type(models.Model):
#     id = models.IntegerField(primary_key=True)
#     quantity = models.IntegerField(blank=True, null=True)
#     name = models.CharField(max_length=30, blank=True, null=True)
#     category = models.ForeignKey(Category, related_name="category_id", on_delete=models.CASCADE, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'type'
