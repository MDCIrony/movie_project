# Generated by Django 4.1.7 on 2023-03-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('years', models.IntegerField()),
                ('rating', models.FloatField()),
                ('genre', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('prince', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateField()),
            ],
            options={
                'db_table': 'movies',
            },
        ),
    ]
