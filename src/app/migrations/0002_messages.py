# Generated by Django 5.1.7 on 2025-03-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('publish', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(blank=True, max_length=254, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Messages',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
