# Generated by Django 5.2.3 on 2025-06-22 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0002_alter_nft_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='img',
            field=models.ImageField(default='', upload_to='uploads/nft'),
        ),
    ]
