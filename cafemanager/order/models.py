from django.db import models


class Order(models.Model):
    table_number = models.IntegerField(verbose_name='Номер стола')
    order_id = models.CharField(max_length=10, unique=True, verbose_name='ID заказа')
    items = models.TextField(verbose_name='Заказанные блюда')
    status = models.CharField(max_length=20, default='в ожидании', verbose_name='Статус')

    def __str__(self):
        return f'Заказ № {self.order_id} на стол № {self.table_number}'