# Generated by Django 3.2.9 on 2021-12-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('file_path', models.CharField(max_length=512, verbose_name='file path')),
                ('url', models.CharField(max_length=512, verbose_name='url')),
                ('bpm', models.IntegerField(verbose_name='bpm')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'Music',
                'verbose_name_plural': 'Musics',
            },
        ),
    ]
