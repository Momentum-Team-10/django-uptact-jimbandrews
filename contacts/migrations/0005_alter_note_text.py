# Generated by Django 3.2.9 on 2021-11-04 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_rename_note_created_note_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(),
        ),
    ]
