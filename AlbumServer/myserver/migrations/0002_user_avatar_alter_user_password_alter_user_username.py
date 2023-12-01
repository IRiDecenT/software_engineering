# Generated by Django 4.2.7 on 2023-11-29 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myserver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(default='http://localhost:8000static/avatar/defaultAvatar.jpg', max_length=256, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=64, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='default', max_length=32, unique=True, verbose_name='用户名'),
        ),
    ]