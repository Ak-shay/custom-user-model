# Generated by Django 2.1.7 on 2019-04-14 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190414_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default='/users/default.png', upload_to='users/profile_pics'),
        ),
    ]
