# Generated by Django 4.1.7 on 2023-03-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0004_pessoa_sobrenome'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='foto',
            field=models.ImageField(default=1, upload_to='foto'),
            preserve_default=False,
        ),
    ]