# Generated by Django 5.0 on 2023-12-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200, verbose_name='نام کامل')),
                ('bio', models.TextField(verbose_name='بیو')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
            ],
            options={
                'verbose_name': 'خواننده',
                'verbose_name_plural': 'خواننده ها',
            },
        ),
        migrations.CreateModel(
            name='UserIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.GenericIPAddressField(verbose_name='آیپی کاربر')),
            ],
            options={
                'verbose_name': 'آیپی کاربر',
                'verbose_name_plural': 'آیپی های کاربران',
            },
        ),
    ]
