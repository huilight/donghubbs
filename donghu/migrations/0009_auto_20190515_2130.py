# Generated by Django 2.1.4 on 2019-05-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donghu', '0008_voter_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_highlight',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='is_sticky',
            field=models.BooleanField(default=False),
        ),
    ]
