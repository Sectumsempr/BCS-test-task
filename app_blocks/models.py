from django.db import models


class Block(models.Model):
    height = models.IntegerField(verbose_name='высота блока')
    hash = models.TextField(verbose_name='хэш блока')
    timestamp = models.IntegerField(verbose_name='время блока')
    miner = models.TextField(verbose_name='адрес майнера')
    transactions_count = models.IntegerField(verbose_name='кол-во транзакций в блоке')
    date = models.DateField(null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'

    def __str__(self):
        return f'{self.height}'
