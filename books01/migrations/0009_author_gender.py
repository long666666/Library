# Generated by Django 3.2.13 on 2022-05-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books01', '0008_remove_publisher_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='gender',
            field=models.IntegerField(choices=[(1, '男'), (2, '女')], default=1),
            preserve_default=False,
        ),
    ]
