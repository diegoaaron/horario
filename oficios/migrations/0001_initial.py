# Generated by Django 4.0.3 on 2022-04-05 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('edad_aproximada', models.IntegerField()),
                ('fecha_rescate', models.DateField()),
            ],
        ),
    ]