# Generated by Django 4.1.1 on 2022-09-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firn', '0003_item_imagem_item_quantidade_alter_item_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='imagem',
            field=models.ImageField(default=None, null=True, upload_to='items'),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantidade',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
