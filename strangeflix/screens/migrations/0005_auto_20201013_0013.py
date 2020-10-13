# Generated by Django 3.1.2 on 2020-10-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0004_auto_20201013_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatus',
            name='plan_type',
            field=models.CharField(blank=True, choices=[('M', 'Monthly'), ('Y', 'Yearly'), ('N', 'No Active Plans')], max_length=2, null=True),
        ),
    ]