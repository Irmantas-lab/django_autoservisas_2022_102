# Generated by Django 4.1.1 on 2022-10-11 06:08

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0005_uzsakymas_terminas_uzsakymas_vartotojas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='automobilis',
            name='aprasymas',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Aprašymas'),
        ),
    ]
