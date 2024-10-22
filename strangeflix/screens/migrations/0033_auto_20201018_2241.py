# Generated by Django 3.1.2 on 2020-10-18 17:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0032_auto_20201018_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='plan_type',
            field=models.CharField(blank=True, choices=[('Y', 'Yearly Plan'), ('H', '6 Months Plan'), ('N', 'No Active Plans'), ('M', 'Monthly Plan')], default='N', max_length=2, null=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='screens.movie')),
            ],
        ),
    ]
