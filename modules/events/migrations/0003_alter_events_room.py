# Generated by Django 4.1 on 2022-08-28 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
        ('events', '0002_rename_cretaed_by_events_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.rooms'),
        ),
    ]