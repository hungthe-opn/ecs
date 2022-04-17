from django.db import models

# Create your models here.
class Employee(models.Model):
    position_id = models.IntegerField()
    department_code = models.CharField(max_length=32,null=True)
    account_id = models.IntegerField()
    job_title_code = models.CharField(max_length=32)
    company_code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20,null=True)
    phone_family = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=255,null=True)
    current_address = models.CharField(max_length=255, null=True)
    gender = models.SmallIntegerField(null=True)
    birthday = models.DateTimeField(null=True)
    other_email = models.CharField(max_length=255, null=True)
    identity_number = models.CharField(max_length=20,null=True)
    identity_card_date = models.DateTimeField(null=True)
    identity_card_place = models.CharField(max_length=255, null=True)
    insurance_number = models.CharField(max_length=20, null=True)
    image_url = models.CharField(max_length=255, null=True)
    link_facebook = models.CharField(max_length=255, null=True)
    nation = models.CharField(max_length=255,null=True)
    nationality = models.CharField(max_length=255, null=True)
    level = models.SmallIntegerField(null=True)
    japanese_level = models.SmallIntegerField(null=True)
    work_type = models.CharField(max_length=64, null=True)
    visa_card_number = models.CharField(max_length=20, null=True)
    visa_date_period = models.DateTimeField(null=True)
    type_of_work_time = models.BooleanField(null=True)
    resignation_date = models.DateTimeField(null=True)
    resignation_reason = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null = True)

    class Meta:
        abstract = True

