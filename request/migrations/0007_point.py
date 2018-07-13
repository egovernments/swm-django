# Generated by Django 2.0.6 on 2018-07-11 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0006_auto_20180711_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(default=12.0)),
                ('lng', models.FloatField(default=77.6)),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('on', models.BooleanField(default=False)),
            ],
        ),
    ]