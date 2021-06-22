# Generated by Django 3.1.3 on 2021-06-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(max_length=200)),
                ('package', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EmailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]