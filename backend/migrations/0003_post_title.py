# Generated by Django 3.0.7 on 2020-06-29 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Default', max_length=100),
            preserve_default=False,
        ),
    ]