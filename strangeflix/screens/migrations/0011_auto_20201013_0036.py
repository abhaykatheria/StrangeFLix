# Generated by Django 3.1.2 on 2020-10-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0010_auto_20201013_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='plan_type',
            field=models.CharField(blank=True, choices=[('Y', 'Yearly'), ('N', 'No Active Plans'), ('M', 'Monthly')], default='N', max_length=2, null=True),
        ),
    ]
