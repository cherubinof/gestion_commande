# Generated by Django 4.2.5 on 2023-09-09 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_produit', '0003_tag_produit_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
