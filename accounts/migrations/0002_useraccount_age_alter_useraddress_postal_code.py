# Generated by Django 5.0 on 2023-12-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='postal_code',
            field=models.IntegerField(),
        ),
    ]
