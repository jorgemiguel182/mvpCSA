# Generated by Django 2.2.2 on 2019-06-28 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190627_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profissional',
            name='sn_consultor',
            field=models.BooleanField(default=False),
        ),
    ]
