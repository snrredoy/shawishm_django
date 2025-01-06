# Generated by Django 5.1.4 on 2025-01-06 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        ('radiologyGroup', '0001_initial'),
        ('referralPhysician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studies',
            fields=[
                ('study_inc_id', models.AutoField(db_column='Study_inc_id', primary_key=True, serialize=False)),
                ('study_inc_id_string', models.CharField(blank=True, db_column='Study_inc_id_string', max_length=50, null=True)),
                ('study_id', models.CharField(blank=True, db_column='Study_id', max_length=50, null=True)),
                ('study_uid', models.CharField(blank=True, db_column='Study_UID', max_length=250, null=True)),
                ('accession_no', models.CharField(blank=True, db_column='Accession_no', max_length=50, null=True)),
                ('study_description', models.CharField(blank=True, db_column='Study_Description', max_length=50, null=True)),
                ('study_uid_url', models.CharField(blank=True, db_column='Study_uid_Url', max_length=200, null=True)),
                ('studydate', models.DateField(blank=True, db_column='StudyDate', null=True)),
                ('study_directory', models.CharField(blank=True, db_column='Study_Directory', max_length=550, null=True)),
                ('procedure_name', models.CharField(blank=True, db_column='Procedure_Name', max_length=45, null=True)),
                ('proc_start', models.DateTimeField(blank=True, db_column='Proc_Start', null=True)),
                ('modality', models.CharField(blank=True, db_column='Modality', max_length=10, null=True)),
                ('received_date', models.DateTimeField(blank=True, db_column='Received_Date', null=True)),
                ('machine_name', models.CharField(blank=True, db_column='Machine_Name', max_length=45, null=True)),
                ('branch_name', models.CharField(blank=True, db_column='Branch_Name', max_length=50, null=True)),
                ('report_url', models.CharField(blank=True, db_column='Report_Url', max_length=200, null=True)),
                ('images', models.IntegerField(blank=True, db_column='Images', null=True)),
                ('series', models.IntegerField(blank=True, db_column='Series', null=True)),
                ('status_reported', models.CharField(blank=True, db_column='Status_Reported', max_length=10, null=True)),
                ('report_verifier', models.CharField(blank=True, db_column='Report_Verifier', max_length=50, null=True)),
                ('institution_name', models.CharField(blank=True, db_column='Institution_Name', max_length=50, null=True)),
                ('study_bodyparts', models.CharField(blank=True, db_column='Study_BodyParts', max_length=200, null=True)),
                ('radiologist_name', models.CharField(blank=True, db_column='Radiologist_Name', max_length=70, null=True)),
                ('radiologist_id', models.IntegerField(blank=True, db_column='Radiologist_ID', null=True)),
                ('othercomments', models.CharField(blank=True, db_column='OtherComments', max_length=450, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('pat_inc_id_det', models.ForeignKey(blank=True, db_column='Pat_inc_id_det', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patients.patients')),
                ('radiology_group', models.ForeignKey(blank=True, db_column='Radiology_Group', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='radiologyGroup.radiologygroup')),
                ('ref_inc', models.ForeignKey(blank=True, db_column='Ref_Inc_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='referralPhysician.referralphysician')),
            ],
        ),
    ]