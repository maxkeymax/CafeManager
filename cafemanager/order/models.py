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
    
    @staticmethod
    def parse_items(items_str):
        """
        Парсит строку с блюдами и ценами.
        Формат: "Блюдо1/100, Блюдо2/200"
        Проверяет корректность введенных данных
        Возвращает список словарей: [{'name': 'Блюдо1', 'price': 100}, ...]
        """
        items = []
        for item in items_str.split(','):
            item = item.strip()
            if '/' in item:
                item, price = item.split('/')
                if not item:
                    raise ValueError(f"Вы не ввели название блюда: {item}")
                try:
                    price = int(price.strip())
                    items.append({'item': item.strip(), 'price': price})
                except ValueError:
                    raise ValueError(f"Некорректная цена в блюде: {item}")
            else:
                raise ValueError(f"Некорректный формат записи блюда и цены: {item}")
        return items
