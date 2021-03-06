# Generated by Django 3.2.4 on 2021-08-21 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola_nomi', models.CharField(max_length=255)),
                ('qisqacha', models.CharField(blank=True, max_length=200)),
                ('matni', models.TextField()),
                ('rasmi', models.ImageField(blank=True, upload_to='images/')),
                ('sanasi', models.DateTimeField(auto_now_add=True)),
                ('muallifi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
