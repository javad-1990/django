# Generated by Django 4.1.4 on 2023-01-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_category_alter_article_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='pages.category', verbose_name='دسته بندی'),
        ),
    ]
