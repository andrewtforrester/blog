# Generated by Django 4.0.8 on 2023-02-04 16:45

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_blogentry_body_delete_commentaryentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='preview',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
    ]
