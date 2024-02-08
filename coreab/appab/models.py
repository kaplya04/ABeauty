from django.db import models


# Create your models here.
class Modal(models.Model):
    id = models.BooleanField
    name = models.TextField(verbose_name="Имя")
    email = models.TextField(verbose_name="Почта")
    number = models.TextField(verbose_name="Номер")
    year = models.TextField(verbose_name="Возраст")

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модель'

    def __str__(self):
        return self.year


class Tovar(models.Model):
    id = models.BooleanField
    name = models.TextField(verbose_name="Имя")
    description = models.TextField(verbose_name="Описание")
    price = models.TextField(verbose_name="Цена")
    photo = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'

    def __str__(self):
        return self.name


class Oplata(models.Model):
    id = models.BooleanField
    name = models.TextField(verbose_name="Имя")
    number = models.CharField(max_length=16, verbose_name="Номер карты", unique=True)
    data = models.DateField(verbose_name="Дата")
    ccv = models.CharField(max_length=3, verbose_name="Три цифры", unique=True)

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата'

    def __str__(self):
        return self.name
