# Generated by Django 4.2.3 on 2023-07-09 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_trainablity_breed_trainability'),
    ]

    operations = [
        migrations.RenameField(
            model_name='breed',
            old_name='exercise_need',
            new_name='exercise_needs',
        ),
    ]
