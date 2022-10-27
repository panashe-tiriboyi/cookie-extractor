# Generated by Django 4.1 on 2022-09-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cookie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie_name', models.CharField(max_length=30)),
                ('cookie_id', models.CharField(max_length=30)),
                ('cookie_value', models.CharField(max_length=30)),
                ('cookie_expiry_date', models.CharField(max_length=30)),
                ('cookie_domain', models.CharField(max_length=30)),
                ('cookie_size', models.CharField(max_length=30)),
                ('cookie_type', models.CharField(max_length=30)),
            ],
        ),
    ]