# Generated by Django 2.0.3 on 2018-03-31 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('phone1', models.CharField(max_length=10)),
                ('phone2', models.CharField(max_length=10)),
                ('phone3', models.CharField(max_length=10)),
            ],
        ),
    ]