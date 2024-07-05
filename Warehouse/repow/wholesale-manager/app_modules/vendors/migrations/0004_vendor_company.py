# Generated by Django 4.1.7 on 2023-06-26 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0001_initial"),
        ("vendors", "0003_alter_vendor_address2_alter_vendor_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="vendor",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="company.company",
                verbose_name="Company",
            ),
        ),
    ]