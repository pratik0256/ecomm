# Generated by Django 5.0 on 2024-01-03 06:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_colorvariant_sizevarient_product_color_variant_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="color_variant",
            field=models.ManyToManyField(blank=True, to="product.colorvariant"),
        ),
        migrations.AlterField(
            model_name="product",
            name="size_variant",
            field=models.ManyToManyField(blank=True, to="product.sizevarient"),
        ),
    ]
