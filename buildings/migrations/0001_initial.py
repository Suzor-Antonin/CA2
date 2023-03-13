# Generated by Django 4.1.5 on 2023-03-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Dorset College', max_length=50)),
                ('floors', models.PositiveSmallIntegerField(default=1)),
                ('color', models.CharField(default='Brick Red', max_length=50)),
                ('residential', models.BooleanField(default=True)),
                ('country', models.CharField(default='Ireland', max_length=20)),
                ('city', models.CharField(default='Dublin', max_length=20)),
                ('street', models.CharField(default='Belvedere Place, Mountjoy Square', max_length=100)),
                ('number', models.CharField(default='7 & 8', max_length=10)),
            ],
        ),
    ]
