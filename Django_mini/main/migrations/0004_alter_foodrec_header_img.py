# Generated by Django 4.1 on 2023-02-26 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_foodrec_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodrec',
            name='header_img',
            field=models.ImageField(blank=True, null=True, upload_to='main/images/%Y/%m/%d/'),
        ),
    ]