# Generated by Django 3.1.2 on 2020-12-17 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name='姓名')),
                ('reciever', models.CharField(max_length=50, verbose_name='收件人')),
                ('subject', models.CharField(max_length=60, verbose_name='主旨')),
                ('content', models.TextField(blank=True, null=True, verbose_name='內容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='留言時間')),
            ],
        ),
    ]
