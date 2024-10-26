# Generated by Django 5.1.2 on 2024-10-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeafImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='leaf_disease_images/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]