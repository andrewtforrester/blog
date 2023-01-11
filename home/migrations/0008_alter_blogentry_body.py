# Generated by Django 3.2.12 on 2023-01-11 01:55

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_blogentry_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('indented_paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, null=True, use_json_field=True),
        ),
    ]