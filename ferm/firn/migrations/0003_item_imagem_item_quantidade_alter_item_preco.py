# Generated by Django 4.1.1 on 2022-09-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firn', '0002_categoria_item_preco_item_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='imagem',
            field=models.ImageField(default=None,null=True,blank=True, upload_to='items'),
        ),
        migrations.AddField(
            model_name='item',
            name='quantidade',
            field=models.IntegerField(default=None,null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]