# Generated by Django 3.1.3 on 2022-05-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='branch',
            field=models.CharField(choices=[('Select Branch', 'Select Branch'), ('CIVIL', 'CIVIL'), ('MECH', 'MECH'), ('ELECT', 'ELECT'), ('TEXT', 'TEXT'), ('IT', 'IT'), ('CSE', 'CSE')], default='Select', max_length=200),
        ),
    ]
