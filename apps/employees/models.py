from django.db import models

# Create your models here.


class AccountModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    is_active = models.IntegerField()
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    is_admin = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class Employees(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    position_id = models.IntegerField()
    department_code = models.ForeignKey('DepartmentModel', to_field='code', db_column='department_code',
                                        on_delete=models.DO_NOTHING, related_name='department_employees')
    account_id = models.IntegerField()
    job_title_code = models.CharField(max_length=32)
    company_code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    phone_family = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    current_address = models.CharField(max_length=255, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    other_email = models.CharField(max_length=255, blank=True, null=True)
    identity_number = models.CharField(max_length=20, blank=True, null=True)
    identity_card_date = models.DateField(blank=True, null=True)
    identity_card_place = models.CharField(max_length=255, blank=True, null=True)
    insurance_number = models.CharField(max_length=20, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    number_of_days_leave = models.FloatField()
    link_facebook = models.CharField(max_length=255, blank=True, null=True)
    nation = models.CharField(max_length=45, blank=True, null=True)
    nationality = models.CharField(max_length=45, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    japanese_level = models.IntegerField(blank=True, null=True)
    work_type = models.CharField(max_length=64, blank=True, null=True)
    visa_card_number = models.CharField(max_length=20, blank=True, null=True)
    visa_date_period = models.DateField(blank=True, null=True)
    university_name = models.CharField(max_length=255, blank=True, null=True)
    type_of_work_time = models.IntegerField(blank=True, null=True)
    join_date = models.DateField()
    resignation_date = models.DateField(blank=True, null=True)
    resignation_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class DepartmentModel(models.Model):
    code = models.CharField(unique=True, max_length=32)
    parent_code = models.CharField(max_length=64, blank=True, null=True)
    company_code = models.CharField(max_length=64, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=255, blank=True, null=True)
    color_code = models.CharField(max_length=10, blank=True, null=True)
    created_by = models.CharField(max_length=4)
    updated_by = models.CharField(max_length=4)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    employee_id = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class AssetEmployeeModel(models.Model):
    employee = models.OneToOneField(Employees, on_delete=models.DO_NOTHING, related_name='fac_employees')
    is_active = models.SmallIntegerField(default=1)
    is_collaborator = models.SmallIntegerField(default=1)

    class Meta:
        managed = True
        db_table = 'asset_employees_tbl'