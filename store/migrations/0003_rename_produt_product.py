# Generated by Django 5.0.1 on 2024-01-26 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_slug'),
        ('store', '0002_alter_produt_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produt',
            new_name='Product',
        ),
    ]