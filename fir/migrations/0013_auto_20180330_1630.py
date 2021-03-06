# Generated by Django 2.0.3 on 2018-03-30 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0012_auto_20180330_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstruc',
            name='status',
            field=models.CharField(default='Unresolved', max_length=10),
        ),
        migrations.AddField(
            model_name='firstruc',
            name='type',
            field=models.CharField(max_length=1000, null=True),
        ),
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
