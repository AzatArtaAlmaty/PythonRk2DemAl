# Generated by Django 2.2.6 on 2019-11-27 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0008_event_geolocation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='pub_date',
            new_name='date',
        ),
    ]
