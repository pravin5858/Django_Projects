# Generated by Django 4.1.7 on 2023-06-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True, null=True)),
                ("updated_at", models.DateField(auto_now_add=True, null=True)),
                ("company_name", models.CharField(max_length=100)),
                ("contact_person", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('address1', models.TextField(blank=True, null=True, verbose_name='Address 1')),
                ('address2', models.TextField(blank=True, null=True, verbose_name='Address 2')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('zip_code', models.IntegerField(verbose_name='Zip Code')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('latitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude')),
                ('longitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
