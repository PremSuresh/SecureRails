# Generated by Django 2.0.3 on 2018-03-30 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0015_auto_20180330_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstruc',
            name='latitude',
            field=models.CharField(default='24.5833', max_length=250),
        ),
        migrations.AlterField(
            model_name='firstruc',
            name='longitude',
            field=models.CharField(default='73.6833', max_length=250),
        ),
        migrations.AlterField(
            model_name='firstruc',
            name='nearest',
            field=models.CharField(default='Udaipur', max_length=250),
        ),
    ]
