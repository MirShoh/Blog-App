# Generated by Django 3.2.4 on 2021-08-21 11:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='matni',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
