# Generated by Django 3.2.3 on 2021-05-28 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20210529_0107'),
        ('authy', '0003_alter_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(to='post.Post'),
        ),
    ]
