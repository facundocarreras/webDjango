# Generated by Django 4.0.3 on 2022-04-11 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTiendaDeportiva', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_familiar', models.CharField(max_length=200)),
                ('edad_familiar', models.IntegerField(max_length=10)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
