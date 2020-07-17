# Generated by Django 3.0.8 on 2020-07-16 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200716_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_info', models.CharField(default='', max_length=50, verbose_name='标题')),
                ('img', models.ImageField(upload_to='banner/', verbose_name='轮番图')),
                ('link_url', models.URLField(max_length=100, verbose_name='图片链接')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否是active')),
            ],
            options={
                'verbose_name': '轮番图',
                'verbose_name_plural': '轮番图',
            },
        ),
    ]
