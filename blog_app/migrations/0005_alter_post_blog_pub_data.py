# Generated by Django 4.2.2 on 2023-09-03 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_alter_post_blog_pub_data_alter_post_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_blog',
            name='pub_data',
            field=models.TimeField(default=datetime.datetime(2023, 9, 3, 8, 58, 35, 740605, tzinfo=datetime.timezone.utc)),
        ),
    ]
