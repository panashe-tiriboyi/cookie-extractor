# Generated by Django 4.1 on 2023-01-23 02:34

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
            ],
        ),
        migrations.CreateModel(
            name='CookieDbTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(max_length=30)),
                ('Platform', models.CharField(max_length=30)),
                ('Category', models.CharField(max_length=30)),
                ('Cookie_or_Data_Key_name_Domain_Description', models.CharField(max_length=30)),
                ('Retention_period', models.CharField(max_length=30)),
                ('Data_ControllerUser_Privacy_and_GDPR_Rights_Portals', models.CharField(max_length=30)),
                ('Wildcard_match', models.CharField(max_length=30)),
            ],
        ),
    ]
