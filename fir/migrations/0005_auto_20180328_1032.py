# Generated by Django 2.0.3 on 2018-03-28 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0004_auto_20180328_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstruc',
            name='latitude',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='firstruc',
            name='longitude',
            field=models.BigIntegerField(null=True),
        ),
    ]
