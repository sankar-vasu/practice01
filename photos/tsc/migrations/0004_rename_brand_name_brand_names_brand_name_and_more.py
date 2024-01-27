# Generated by Django 4.2.6 on 2023-10-13 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsc', '0003_brand_names_alter_photo_upload_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand_names',
            old_name='brand_name',
            new_name='brand_Name',
        ),
        migrations.AlterField(
            model_name='brand_names',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 13, 18, 28, 46, 527250)),
        ),
        migrations.AlterField(
            model_name='photo_upload',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 13, 18, 28, 46, 527250)),
        ),
        migrations.AlterField(
            model_name='tsc_stores',
            name='store_createdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 13, 18, 28, 46, 527250)),
        ),
    ]