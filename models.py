# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
#
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
#
#
# class Lend(models.Model):
#     lend_id = models.CharField(db_column='LEND_ID', primary_key=True, max_length=4)  # Field name made lowercase.
#     stt = models.IntegerField(db_column='STT')  # Field name made lowercase.
#     device_code = models.CharField(db_column='DEVICE_CODE', max_length=45)  # Field name made lowercase.
#     rent_time = models.DateField(db_column='RENT_TIME', blank=True, null=True)  # Field name made lowercase.
#     pay_time = models.DateField(db_column='PAY_TIME', blank=True, null=True)  # Field name made lowercase.
#     describe = models.CharField(db_column='DESCRIBE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     quantity = models.IntegerField(db_column='QUANTITY', blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     insurance_start = models.DateField(db_column='INSURANCE_START', blank=True, null=True)  # Field name made lowercase.
#     insurance_end = models.DateField(db_column='INSURANCE_END', blank=True, null=True)  # Field name made lowercase.
#     warranty = models.CharField(db_column='WARRANTY', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     condition = models.CharField(db_column='CONDITION', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     id = models.ForeignKey(Employees, models.DO_NOTHING, db_column='ID')  # Field name made lowercase.
#     product = models.ForeignKey('Repository', models.DO_NOTHING, db_column='PRODUCT_ID')  # Field name made lowercase.
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'lend'
#
#
# class Manage(models.Model):
#     manage_id = models.AutoField(db_column='MANAGE_ID', primary_key=True)  # Field name made lowercase.
#     goods_receipt = models.CharField(db_column='GOODS_RECEIPT', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     import_date = models.DateField(db_column='IMPORT_DATE', blank=True, null=True)  # Field name made lowercase.
#     export = models.CharField(db_column='EXPORT', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     export_date = models.DateField(db_column='EXPORT_DATE', blank=True, null=True)  # Field name made lowercase.
#     quantity = models.IntegerField(db_column='QUANTITY')  # Field name made lowercase.
#     reason = models.CharField(db_column='REASON', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     status = models.IntegerField(db_column='STATUS')  # Field name made lowercase.
#     status_manage = models.CharField(db_column='STATUS_MANAGE', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     lend = models.ForeignKey(Lend, models.DO_NOTHING, db_column='LEND_ID')  # Field name made lowercase.
#     id = models.ForeignKey(Employees, models.DO_NOTHING, db_column='ID')  # Field name made lowercase.
#     product = models.ForeignKey('Repository', models.DO_NOTHING, db_column='PRODUCT_ID')  # Field name made lowercase.
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'manage'
#
#
# class Repository(models.Model):
#     product_id = models.CharField(db_column='PRODUCT_ID', primary_key=True, max_length=10)  # Field name made lowercase.
#     name = models.CharField(db_column='NAME', max_length=30)  # Field name made lowercase.
#     quantity = models.IntegerField(db_column='QUANTITY', blank=True, null=True)  # Field name made lowercase.
#     color = models.CharField(db_column='COLOR', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     lend_device = models.IntegerField(db_column='LEND_DEVICE')  # Field name made lowercase.
#     sum_device = models.IntegerField(db_column='SUM_DEVICE')  # Field name made lowercase.
#     residual = models.IntegerField(db_column='RESIDUAL')  # Field name made lowercase.
#     floor = models.IntegerField(db_column='FLOOR', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     type = models.ForeignKey('Type', models.DO_NOTHING, db_column='TYPE_ID', blank=True, null=True)  # Field name made lowercase.
#     updated_at = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'repository'
#
#
# class Type(models.Model):
#     type_id = models.CharField(db_column='TYPE_ID', primary_key=True, max_length=4)  # Field name made lowercase.
#     quantity = models.IntegerField(db_column='QUANTITY', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(db_column='NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     category = models.ForeignKey(Category, models.DO_NOTHING, db_column='CATEGORY_ID', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'type'
