# Generated by Django 4.0.8 on 2023-02-04 16:18

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_commentaryentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('indented_paragraph', wagtail.blocks.RichTextBlock()), ('commentary_block', wagtail.blocks.StructBlock([('column_1', wagtail.blocks.RichTextBlock()), ('column_2', wagtail.blocks.RichTextBlock())])), ('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, null=True, use_json_field=True),
        ),
        migrations.DeleteModel(
            name='CommentaryEntry',
        ),
    ]