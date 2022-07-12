# Generated by Django 4.0.4 on 2022-07-09 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0008_rename_descripcion_producto_descripcion_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria_producto',
            field=models.CharField(choices=[('alimentos', 'alimentos'), ('correas', 'correas'), ('higiene', 'higiene'), ('bandanas', 'bandanas'), ('ropa', 'ropa'), ('identificadores', 'identificadores')], default='default_value', max_length=50),
        ),
    ]