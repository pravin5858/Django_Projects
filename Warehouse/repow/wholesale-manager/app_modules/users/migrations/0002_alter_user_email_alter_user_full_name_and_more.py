# Generated by Django 4.1.7 on 2023-06-21 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="user",
            name="full_name",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Full Name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Phone"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("super admin", "Super Admin"),
                    ("admin", "Admin"),
                    ("company admin", "Company Admin"),
                    ("sales representative", "Sales Representative"),
                    ("driver", "Driver"),
                ],
                default="admin",
                max_length=20,
                verbose_name="Role",
            ),
        ),
    ]
