# Generated by Django 3.1.4 on 2021-01-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassMentor', '0002_auto_20201227_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]