# Generated by Django 4.2.5 on 2023-09-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_produit', '0002_alter_produit_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='tag',
            field=models.ManyToManyField(to='app_produit.tag'),
        ),
    ]