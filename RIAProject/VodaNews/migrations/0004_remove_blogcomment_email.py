# Generated by Django 4.1.5 on 2023-02-01 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VodaNews', '0003_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='email',
        ),
    ]
