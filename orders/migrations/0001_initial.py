# Generated by Django 3.2.9 on 2021-12-01 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=225)),
                ('document', models.CharField(max_length=225)),
                ('message', models.TextField()),
                ('created_on', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
