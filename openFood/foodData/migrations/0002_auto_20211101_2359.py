# Generated by Django 3.2.8 on 2021-11-02 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodData', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_datetime',
        ),
        migrations.RemoveField(
            model_name='product',
            name='last_modified_datetime',
        ),
    ]
