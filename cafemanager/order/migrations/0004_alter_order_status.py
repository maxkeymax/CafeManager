# Generated by Django 4.2.18 on 2025-01-28 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('В ожидании', 'В ожидании'), ('Готово', 'Готово'), ('Оплачено', 'Оплачено')], default='В ожидании', max_length=10, verbose_name='Статус'),
        ),
    ]
