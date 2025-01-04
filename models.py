# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RadiologyGroup(models.Model):
    rg_inc_id = models.PositiveBigIntegerField(db_column='RG_Inc_ID', primary_key=True)  # Field name made lowercase.
    rg_id = models.IntegerField(db_column='RG_ID', blank=True, null=True)  # Field name made lowercase.
    rg_name = models.CharField(db_column='RG_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rg_members = models.CharField(db_column='RG_Members', max_length=100, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'radiology_group'


class Studies(models.Model):
    study_inc_id = models.AutoField(db_column='Study_inc_id', primary_key=True)  # Field name made lowercase.
    study_inc_id_string = models.CharField(db_column='Study_inc_id_string', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accession_no = models.CharField(db_column='Accession_no', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pat_inc_id_det = models.ForeignKey(Patients, models.DO_NOTHING, db_column='Pat_inc_id_det', blank=True, null=True)  # Field name made lowercase.
    pat_id = models.CharField(db_column='Pat_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    study_id = models.CharField(db_column='Study_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    study_description = models.CharField(db_column='Study_Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    study_uid_url = models.CharField(db_column='Study_uid_Url', max_length=200, blank=True, null=True)  # Field name made lowercase.
    studydate = models.DateField(db_column='StudyDate', blank=True, null=True)  # Field name made lowercase.
    ref_phy_name = models.CharField(max_length=50, blank=True, null=True)
    study_directory = models.CharField(db_column='Study_Directory', max_length=550, blank=True, null=True)  # Field name made lowercase.
    ref_inc = models.ForeignKey(Referralphysician, models.DO_NOTHING, db_column='Ref_Inc_ID', blank=True, null=True)  # Field name made lowercase.
    ref_id = models.CharField(db_column='Ref_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    procedure_name = models.CharField(db_column='Procedure_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    proc_start = models.DateTimeField(db_column='Proc_Start', blank=True, null=True)  # Field name made lowercase.
    modality = models.CharField(db_column='Modality', max_length=10, blank=True, null=True)  # Field name made lowercase.
    received_date = models.DateTimeField(db_column='Received_Date', blank=True, null=True)  # Field name made lowercase.
    machine_name = models.CharField(db_column='Machine_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    study_uid = models.CharField(db_column='Study_UID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    branch_name = models.CharField(db_column='Branch_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    report_url = models.CharField(db_column='Report_Url', max_length=200, blank=True, null=True)  # Field name made lowercase.
    images = models.IntegerField(db_column='Images', blank=True, null=True)  # Field name made lowercase.
    series = models.IntegerField(db_column='Series', blank=True, null=True)  # Field name made lowercase.
    status_reported = models.CharField(db_column='Status_Reported', max_length=10, blank=True, null=True)  # Field name made lowercase.
    report_verifier = models.CharField(db_column='Report_Verifier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    institution_name = models.CharField(db_column='Institution_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    study_bodyparts = models.CharField(db_column='Study_BodyParts', max_length=200, blank=True, null=True)  # Field name made lowercase.
    radiologist_name = models.CharField(db_column='Radiologist_Name', max_length=70, blank=True, null=True)  # Field name made lowercase.
    radiologist_id = models.IntegerField(db_column='Radiologist_ID', blank=True, null=True)  # Field name made lowercase.
    radiology_group = models.CharField(db_column='Radiology_Group', max_length=45, blank=True, null=True)  # Field name made lowercase.
    othercomments = models.CharField(db_column='OtherComments', max_length=450, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studies'


class Users(models.Model):
    u_inc_id = models.BigAutoField(db_column='U_Inc_ID', primary_key=True)  # Field name made lowercase.
    u_id = models.IntegerField(db_column='U_ID', blank=True, null=True)  # Field name made lowercase.
    u_name = models.CharField(db_column='U_name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    u_fullname = models.CharField(db_column='U_fullname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    u_email = models.CharField(db_column='U_email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    u_sex = models.CharField(db_column='U_sex', max_length=45, blank=True, null=True)  # Field name made lowercase.
    remember_token = models.CharField(max_length=255, blank=True, null=True)
    u_address = models.CharField(db_column='U_address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    u_role = models.CharField(db_column='U_Role', max_length=45, blank=True, null=True)  # Field name made lowercase.
    u_phone = models.CharField(db_column='U_phone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    u_password = models.CharField(db_column='U_password', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rg_id = models.CharField(db_column='RG_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
