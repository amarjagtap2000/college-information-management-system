# Generated by Django 3.1.3 on 2022-05-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_auto_20220525_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherextra',
            name='teacher_profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/TeacherProfile_pic/'),
        ),
    ]