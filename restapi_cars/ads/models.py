from django.db import models


class Cars(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('наименование', max_length=200)
    title = models.TextField('Описание',blank=True)
    year = models.IntegerField('Год')
    price = models.IntegerField('Цена')
    link = models.TextField('Ссылка')
    created_on = models.DateTimeField('ДатаСоздания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Машины'
        verbose_name_plural = 'Машины'









