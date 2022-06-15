# Generated by Django 4.0.4 on 2022-06-15 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('sub_titulo', models.CharField(max_length=100)),
                ('cuerpo', models.TextField()),
                ('autor', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
