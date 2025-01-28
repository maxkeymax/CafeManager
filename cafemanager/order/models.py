from django.db import models


class Order(models.Model):
    STATUS_CHOISES = [
        ('В ожидании', 'В ожидании'),
        ('Готово', 'Готово'),
        ('Оплачено', 'Оплачено')
    ]
    table_number = models.IntegerField(verbose_name='Номер стола')
    items = models.TextField(verbose_name='Заказанные блюда')
    total_price = models.IntegerField(verbose_name='Общая стоимость', default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOISES, default='В ожидании', verbose_name='Статус')

    def __str__(self):
        return f'Заказ № {self.id} на стол № {self.table_number} статус: {self.status}'