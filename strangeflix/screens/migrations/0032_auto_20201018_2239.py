# Generated by Django 3.1.2 on 2020-10-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0031_auto_20201016_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='plan_type',
            field=models.CharField(blank=True, choices=[('M', 'Monthly Plan'), ('H', '6 Months Plan'), ('Y', 'Yearly Plan'), ('N', 'No Active Plans')], default='N', max_length=2, null=True),
        ),
    ]
