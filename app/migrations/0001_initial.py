# Generated by Django 3.1.3 on 2021-01-26 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tblLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventdatetime', models.DateTimeField(blank=True, verbose_name='Event Date Time')),
                ('eventname', models.CharField(blank=True, max_length=50, verbose_name='Event Name')),
                ('description', models.CharField(blank=True, max_length=190, verbose_name='Desc')),
                ('transfduration', models.FloatField(verbose_name='Trasfer Duration')),
                ('fromhost', models.CharField(blank=True, max_length=50, verbose_name='From Host')),
                ('tohost', models.CharField(blank=True, max_length=50, verbose_name='To Host')),
                ('comments', models.CharField(blank=True, max_length=190, verbose_name='Comments')),
            ],
            options={
                'db_table': 'tblLogs',
                'managed': False,
            },
        ),
    ]
