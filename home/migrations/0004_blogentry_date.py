# Generated by Django 3.2.12 on 2023-01-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_blogentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Post date'),
        ),
    ]
