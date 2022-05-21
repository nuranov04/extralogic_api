# Generated by Django 4.0.4 on 2022-05-20 19:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название формы')),
                ('description', models.TextField(verbose_name='описание формы')),
                ('form_uid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'форма',
                'verbose_name_plural': 'формы',
                'ordering': ('-id',),
            },
        ),
    ]