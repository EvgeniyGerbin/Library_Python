# Generated by Django 4.2.2 on 2023-07-17 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("authors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=200)),
                (
                    "poster",
                    models.ImageField(
                        blank=True, null=True, upload_to="books/posters/"
                    ),
                ),
                ("publication_date", models.DateField()),
                ("is_available", models.BooleanField(default=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="authors.author"
                    ),
                ),
            ],
        ),
    ]