# Generated by Django 5.0.2 on 2024-02-12 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('web_developer', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
