# Generated by Django 2.0.3 on 2018-03-28 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0005_auto_20180328_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstruc',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='firstruc',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
