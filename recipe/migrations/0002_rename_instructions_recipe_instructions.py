# Generated by Django 4.0.2 on 2022-02-03 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='Instructions',
            new_name='instructions',
        ),
    ]
