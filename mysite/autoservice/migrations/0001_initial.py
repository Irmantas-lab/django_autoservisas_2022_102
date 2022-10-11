# Generated by Django 4.1.1 on 2022-10-03 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutomobilioModelis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamintojas', models.CharField(max_length=100, verbose_name='Gamintojas')),
                ('modelis', models.CharField(max_length=100, verbose_name='Modelis')),
            ],
        ),
        migrations.CreateModel(
            name='Automobilis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valstybinis_nr', models.CharField(max_length=10, verbose_name='Valstybinis numeris')),
                ('vin_kodas', models.CharField(max_length=20, verbose_name='VIN kodas')),
                ('kliento_vardas', models.CharField(max_length=30, verbose_name='Kliento vardas')),
                ('modelis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.automobiliomodelis')),
            ],
        ),
        migrations.CreateModel(
            name='Paslauga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavadinimas', models.CharField(max_length=200, verbose_name='Pavadinimas')),
                ('kaina', models.FloatField(verbose_name='Kaina')),
            ],
        ),
        migrations.CreateModel(
            name='Uzsakymas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data')),
                ('automobilis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.automobilis')),
            ],
        ),
        migrations.CreateModel(
            name='UzsakymoEilute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kiekis', models.IntegerField(verbose_name='Kiekis')),
                ('paslauga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.paslauga')),
                ('uzsakymas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autoservice.uzsakymas')),
            ],
        ),
    ]
