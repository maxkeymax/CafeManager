from django.db import models


class Order(models.Model):
    STATUS_CHOISES = [
        ('в ожидании', 'В ожидании'),
        ('готово', 'Готово'),
        ('оплачено', 'Оплачено')
    ]
    table_number = models.IntegerField(verbose_name='Номер стола')
    items = models.TextField(verbose_name='Заказанные блюда')
    total_price = models.IntegerField(verbose_name='Общая стоимость', default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOISES, default='в ожидании', verbose_name='Статус')

    def __str__(self):
        return f'Заказ № {self.id} на стол № {self.table_number} статус: {self.status}'