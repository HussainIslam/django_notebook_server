# Generated by Django 3.0.8 on 2020-08-01 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Normal', 'Normal'), ('Low', 'Low')], default='Normal', max_length=10),
        ),
    ]