# Generated by Django 4.0.5 on 2022-09-19 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='static/pro_images/user-icon.jpg', upload_to='images'),
        ),
    ]
