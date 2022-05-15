# Generated by Django 3.2.13 on 2022-05-14 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books01', '0005_auto_20220514_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='books01.Author'),
        ),
    ]
