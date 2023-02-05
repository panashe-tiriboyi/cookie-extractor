# Generated by Django 4.1 on 2023-01-24 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_clientdomains'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie_domain', models.CharField(db_index=True, max_length=30, unique=True)),
                ('date_last_added', models.DateField(auto_now=True)),
            ],
        ),
    ]
