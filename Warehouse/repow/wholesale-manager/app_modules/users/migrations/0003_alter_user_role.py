# Generated by Django 4.1.7 on 2023-06-26 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_email_alter_user_full_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("super admin", "Super Admin"),
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