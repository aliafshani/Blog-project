# Generated by Django 4.2.2 on 2023-09-03 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_alter_post_blog_pub_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_blog',
            name='pub_data',
            field=models.TimeField(default=datetime.datetime(2023, 9, 3, 9, 1, 34, 286100, tzinfo=datetime.timezone.utc)),
        ),
    ]