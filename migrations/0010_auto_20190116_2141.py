# Generated by Django 2.1.1 on 2019-01-16 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0009_auto_20180924_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(blank=True, default=None, max_length=2000, null=True, verbose_name='Message'),
        ),
    ]