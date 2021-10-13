# Generated by Django 3.2.4 on 2021-10-12 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='images')),
                ('file', models.FileField(upload_to='files')),
            ],
        ),
    ]
