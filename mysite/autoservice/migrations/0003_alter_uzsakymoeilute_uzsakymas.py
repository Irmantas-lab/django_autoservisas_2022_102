# Generated by Django 4.1.1 on 2022-10-06 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0002_alter_automobiliomodelis_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzsakymoeilute',
            name='uzsakymas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eilutes', to='autoservice.uzsakymas'),
        ),
    ]
