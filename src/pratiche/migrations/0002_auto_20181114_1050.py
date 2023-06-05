# Generated by Django 2.1.2 on 2018-11-14 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratiche', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='magistrato',
            name='cellulare',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='magistrato',
            name='nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='magistrato',
            name='tel_ufficio',
            field=models.CharField(default='No', max_length=15),
        ),
        migrations.AddField(
            model_name='magistrato',
            name='ufficio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='magistrato',
            name='cognome',
            field=models.CharField(max_length=50),
        ),
    ]