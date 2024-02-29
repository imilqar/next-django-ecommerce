# Generated by Django 5.0.2 on 2024-02-29 10:56

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductSpecification",
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
                (
                    "name",
                    models.CharField(
                        help_text="Required", max_length=255, verbose_name="Name"
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Specification",
                "verbose_name_plural": "Product Specifications",
            },
        ),
        migrations.CreateModel(
            name="ProductType",
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
                (
                    "name",
                    models.CharField(
                        help_text="Required and unique",
                        max_length=255,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Product Type",
                "verbose_name_plural": "Product Types",
            },
        ),
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(
                        help_text="Required and unique",
                        max_length=255,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="Slug"),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="store.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "name",
                    models.CharField(
                        help_text="Required", max_length=255, verbose_name="Name"
                    ),
                ),
                ("desc", models.TextField(blank=True, verbose_name="Description")),
                ("slug", models.SlugField(max_length=255)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "The price must be between 0 and 999.99."
                            }
                        },
                        help_text="Maximum 999.99",
                        max_digits=5,
                        verbose_name="Price",
                    ),
                ),
                (
                    "discount_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "The price must be between 0 and 999.99."
                            }
                        },
                        help_text="Maximum 999.99",
                        max_digits=5,
                        verbose_name="Discount price",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Change visibility",
                        verbose_name="Product visibility",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="store.category",
                    ),
                ),
                (
                    "product_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="store.producttype",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                (
                    "image",
                    models.ImageField(
                        default="images/default.png",
                        help_text="Upload a product image",
                        upload_to="images/",
                        verbose_name="Image",
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Alternative text",
                    ),
                ),
                ("is_feature", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_image",
                        to="store.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Image",
                "verbose_name_plural": "Product Images",
            },
        ),
        migrations.CreateModel(
            name="ProductSpecificationValue",
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
                (
                    "value",
                    models.CharField(
                        help_text="Product specification value (maximum of 255 words",
                        max_length=255,
                        verbose_name="Value",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.product"
                    ),
                ),
                (
                    "specification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="store.productspecification",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Specification Value",
                "verbose_name_plural": "Product Specification Values",
            },
        ),
        migrations.AddField(
            model_name="productspecification",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="store.producttype"
            ),
        ),
    ]