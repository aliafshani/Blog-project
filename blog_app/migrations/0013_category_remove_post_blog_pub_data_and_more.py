# Generated by Django 4.2.2 on 2023-09-04 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0012_alter_post_blog_pub_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('crerated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post_blog',
            name='pub_data',
        ),
        migrations.AlterField(
            model_name='post_blog',
            name='title',
            field=models.CharField(max_length=70),
        ),
        migrations.AddField(
            model_name='post_blog',
            name='category',
            field=models.ManyToManyField(to='blog_app.category'),
        ),
    ]