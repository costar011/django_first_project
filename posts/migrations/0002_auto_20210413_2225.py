# Generated by Django 3.2 on 2021-04-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'verbose_name_plural': '게시글 관리'},
        ),
        migrations.AddField(
            model_name='postmodel',
            name='thumbnali',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
