# Generated by Django 3.1.2 on 2020-10-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0033_auto_20201018_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='plan_type',
            field=models.CharField(blank=True, choices=[('Y', 'Yearly Plan'), ('N', 'No Active Plans'), ('M', 'Monthly Plan'), ('H', '6 Months Plan')], default='N', max_length=2, null=True),
        ),
    ]
