# Generated by Django 5.1.4 on 2025-01-06 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='pat_inc_id_string',
            field=models.CharField(blank=True, db_column='Pat_inc_id_string', max_length=50, null=True),
        ),
    ]