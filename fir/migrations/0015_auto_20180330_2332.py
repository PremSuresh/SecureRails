# Generated by Django 2.0.3 on 2018-03-30 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0014_auto_20180330_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstruc',
            name='latitude',
            field=models.CharField(default='28.5355', max_length=250),
        ),
        migrations.AlterField(
            model_name='firstruc',
            name='longitude',
            field=models.CharField(default='77.391', max_length=250),
        ),
        migrations.AlterField(
            model_name='firstruc',
            name='nearest',
            field=models.CharField(default='Delhi', max_length=250),
        ),
    ]
