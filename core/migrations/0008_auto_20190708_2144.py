# Generated by Django 2.2.3 on 2019-07-09 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190630_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profissional',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='media/%m/%d'),
        ),
    ]