# Generated by Django 4.1 on 2023-01-23 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(max_length=30)),
                ('Platform', models.CharField(max_length=30)),
                ('Category', models.CharField(max_length=30)),
                ('Cookie_or_Data_Key_name', models.CharField(max_length=30)),
                ('Domain', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('Retention_period', models.CharField(max_length=30)),
                ('Data_Controller', models.CharField(max_length=30)),
                ('User_Privacy_and_GDPR_Rights_Portals', models.CharField(max_length=30)),
                ('Wildcard_match', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CookieDbTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(max_length=30)),
                ('Platform', models.CharField(max_length=30)),
                ('Category', models.CharField(max_length=30)),
                ('Cookie_or_Data_Key_name', models.CharField(max_length=30)),
                ('Domain', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('Retention_period', models.CharField(max_length=30)),
                ('Data_Controller', models.CharField(max_length=30)),
                ('User_Privacy_and_GDPR_Rights_Portals', models.CharField(max_length=30)),
                ('Wildcard_match', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CookieDbTest1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(max_length=30)),
                ('Platform', models.CharField(max_length=30)),
                ('Category', models.CharField(max_length=30)),
                ('Cookie_or_Data_Key_name', models.CharField(max_length=30)),
                ('Domain', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('Retention_period', models.CharField(max_length=30)),
                ('Data_Controller', models.CharField(max_length=30)),
                ('User_Privacy_and_GDPR_Rights_Portals', models.CharField(max_length=30)),
                ('Wildcard_match', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CookieDbTest2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(max_length=30)),
                ('Platform', models.CharField(max_length=30)),
                ('Category', models.CharField(max_length=30)),
                ('Cookie_or_Data_Key_name', models.CharField(max_length=30)),
                ('Domain', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('Retention_period', models.CharField(max_length=30)),
                ('Data_Controller', models.CharField(max_length=30)),
                ('User_Privacy_and_GDPR_Rights_Portals', models.CharField(max_length=30)),
                ('Wildcard_match', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CookieDbTest3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(max_length=30)),
                ('Platform', models.CharField(max_length=30)),
                ('Category', models.CharField(max_length=30)),
                ('Cookie_or_Data_Key_name', models.CharField(max_length=30)),
                ('Domain', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('Retention_period', models.CharField(max_length=30)),
                ('Data_Controller', models.CharField(max_length=30)),
                ('User_Privacy_and_GDPR_Rights_Portals', models.CharField(max_length=30)),
                ('Wildcard_match', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CookieDbTest4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(max_length=30)),
                ('Platform', models.CharField(max_length=30)),
                ('Category', models.CharField(max_length=30)),
                ('Cookie_or_Data_Key_name', models.CharField(max_length=30)),
                ('Domain', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('Retention_period', models.CharField(max_length=30)),
                ('Data_Controller', models.CharField(max_length=30)),
                ('User_Privacy_and_GDPR_Rights_Portals', models.CharField(max_length=30)),
                ('Wildcard_match', models.CharField(max_length=30)),
            ],
        ),
    ]
