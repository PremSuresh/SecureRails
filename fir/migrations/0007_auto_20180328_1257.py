# Generated by Django 2.0.3 on 2018-03-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0006_auto_20180328_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstruc',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='firstruc',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=6, null=True),
        ),
    ]
