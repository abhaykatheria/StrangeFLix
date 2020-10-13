# Generated by Django 3.1.2 on 2020-10-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0021_auto_20201013_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='plan_type',
            field=models.CharField(choices=[('Y', 'Yearly Plan'), ('M', 'Monthly Plan'), ('N', 'No Active Plans'), ('H', '6 Months Plan')], default='N', max_length=2),
        ),
    ]