# Generated by Django 4.2.7 on 2023-12-08 19:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('notes', models.TextField()),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
