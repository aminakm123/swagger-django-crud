# Generated by Django 5.1.3 on 2024-12-04 13:48

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=125, verbose_name='Category Name')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is this category deleted?')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, verbose_name='Product Name')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='uploads/products/', verbose_name='Image')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is this product deleted?')),
                ('category', models.ForeignKey(limit_choices_to={'is_deleted': False}, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['name'],
            },
        ),
    ]
