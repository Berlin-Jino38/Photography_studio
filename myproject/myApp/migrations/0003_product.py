# Generated by Django 4.2.5 on 2023-09-15 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_registermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('product_image', models.ImageField(upload_to='images')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.gallerymodel')),
            ],
        ),
    ]