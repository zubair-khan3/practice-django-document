# Generated by Django 3.1.5 on 2021-04-11 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
    ]
