# Generated by Django 5.0.1 on 2024-01-26 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produt',
            name='images',
            field=models.ImageField(blank=True, upload_to='photos/products'),
        ),
    ]