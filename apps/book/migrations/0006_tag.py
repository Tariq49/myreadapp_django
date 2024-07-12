# Generated by Django 5.0.6 on 2024-07-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0005_alter_book_authors"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]