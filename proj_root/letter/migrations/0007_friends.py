# Generated by Django 4.2.1 on 2023-06-27 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0006_letteruser_alter_letter_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_nick', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('friend_email', models.EmailField(max_length=254, verbose_name='Friend Email')),
            ],
        ),
    ]
