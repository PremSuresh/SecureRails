# Generated by Django 2.0.3 on 2018-03-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0002_auto_20180328_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='constable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('pnr', models.CharField(max_length=100)),
            ],
        ),
    ]
