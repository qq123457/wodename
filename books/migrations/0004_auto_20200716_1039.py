# Generated by Django 3.0.8 on 2020-07-16 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20200716_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='article_img/%Y/%m/%d/', verbose_name='书籍封面'),
        ),
    ]
