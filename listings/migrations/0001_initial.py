# Generated by Django 5.1 on 2024-09-04 11:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Electronics', 'Electronics'), ('Furniture', 'Furniture'), ('Clothing', 'Clothing'), ('Books', 'Books'), ('Food', 'Food'), ('Food_Items', 'Food Items'), ('Health', 'Health'), ('Other', 'Other')], max_length=20)),
                ('images', models.ImageField(blank=True, null=True, upload_to='listing_images/')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
