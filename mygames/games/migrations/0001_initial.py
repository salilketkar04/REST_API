# Generated by Django 4.0.1 on 2022-01-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.IntegerField()),
                ('publisher', models.CharField(max_length=100)),
                ('platforms', models.TextField()),
                ('modes', models.TextField()),
            ],
        ),
    ]
