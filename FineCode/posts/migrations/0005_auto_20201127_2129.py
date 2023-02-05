# Generated by Django 3.1.3 on 2020-11-27 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_assignment_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='marks',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='submittedassignment',
            name='grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='submittedassignment',
            name='is_reviewed',
            field=models.BooleanField(default=False),
        ),
    ]
