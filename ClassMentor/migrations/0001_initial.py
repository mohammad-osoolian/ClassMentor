# Generated by Django 3.1.4 on 2020-12-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ostad', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
