# Generated by Django 3.0.6 on 2020-05-25 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamapplication',
            name='participation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.Participation'),
        ),
    ]