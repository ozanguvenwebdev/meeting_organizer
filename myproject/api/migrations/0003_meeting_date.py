# Generated by Django 5.0 on 2023-12-05 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_explanation_meeting_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]