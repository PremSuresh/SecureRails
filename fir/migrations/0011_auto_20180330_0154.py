# Generated by Django 2.0.3 on 2018-03-29 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0010_auto_20180329_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstruc',
            name='latitude',
            field=models.CharField(default='8.1939', max_length=250),
        ),
        migrations.AlterField(
            model_name='firstruc',
            name='longitude',
            field=models.CharField(default='77.4314', max_length=250),
        ),
        migrations.AlterField(
            model_name='firstruc',
            name='nearest',
            field=models.CharField(default='625.7746497657419', max_length=250),
        ),
    ]