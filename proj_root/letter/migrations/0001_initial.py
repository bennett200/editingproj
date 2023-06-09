# Generated by Django 4.2.1 on 2023-06-09 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_to', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('ending', models.CharField(max_length=50)),
            ],
        ),
    ]
