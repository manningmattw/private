# Generated by Django 2.0.6 on 2018-06-07 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doubloon', '0003_auto_20180606_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentvalues',
            old_name='deprecated',
            new_name='depreciated',
        ),
    ]