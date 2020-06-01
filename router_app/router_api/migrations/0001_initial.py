# Generated by Django 2.2.9 on 2020-06-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sapid', models.CharField(max_length=30, null=True, unique=True)),
                ('hostname', models.CharField(max_length=100, null=True, unique=True)),
                ('loopback', models.CharField(max_length=100, null=True, unique=True)),
                ('mac_address', models.CharField(max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'router',
            },
        ),
    ]