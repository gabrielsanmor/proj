# Generated by Django 4.1.1 on 2022-09-28 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firn', '0008_remove_item_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='imagem',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='items'),
        ),
    ]
