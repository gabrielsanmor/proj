# Generated by Django 4.1.1 on 2022-09-28 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firn', '0004_alter_item_imagem_alter_item_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='imagem',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='items'),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantidade',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
