# Generated by Django 3.1.2 on 2020-11-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_tune_successful_guessers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tune',
            name='source',
        ),
        migrations.AddField(
            model_name='tune',
            name='answer',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
