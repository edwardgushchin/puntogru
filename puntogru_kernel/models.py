#! coding: utf-8

from __future__ import unicode_literals
import os
from uuid import uuid1
from django.db import models

def get_file_path(instance, filename):
    result = os.path.join('portfolio', uuid1().hex)
    if '.' in filename:
        result = '%s.%s' % (result, filename.split('.')[-1])
        return result

class Portfolio(models.Model):
    APARTMENT = 'AP'
    HOUSE = 'HO'
    RESTAURANT = 'RE'
    OFFICE = 'OF'
    HOTEL = 'HOT'

    INTERIOR_CHOICES = (
        (APARTMENT, u'Интерьер квартир'),
        (HOUSE, u'Интерьер дома, котеджа'),
        (RESTAURANT, u'Интерьеры ресторанов, кафе, баров'),
        (OFFICE, u'Интерьеры офисов, магазинов'),
        (HOTEL, u'Интерьер отеля'),
    )

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    interior = models.CharField(max_length=3, choices=INTERIOR_CHOICES, default=APARTMENT, verbose_name='Тип')
    img = models.ImageField(verbose_name='Изображение')

    def photo_list(self):
        return PortfolioPhoto.objects.filter(portfolio=self)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'работу'
        verbose_name_plural = 'Наши работы'

class PortfolioPhoto(models.Model):
    photo = models.ImageField(verbose_name='Фотография портфолио', upload_to=get_file_path)
    portfolio = models.ForeignKey(Portfolio, verbose_name='Портфолио')

    class Meta:
        verbose_name = 'фотографию'

 
class Services(models.Model):
    title = models.CharField(max_length=29, verbose_name='Заголовок')
    descript = models.CharField(max_length=350, verbose_name='Описание')
    img = models.ImageField(verbose_name='Изображение')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'услугу'
        verbose_name_plural = 'Услуги'

class Reviews(models.Model):
    text = models.TextField(verbose_name='Текст')
    autor = models.CharField(max_length=100, verbose_name='Автор')
    avatar = models.ImageField(verbose_name='Аватар')

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'

class HowWeWork(models.Model):
    title = models.CharField(max_length=29, verbose_name='Заголовок')
    descript = models.CharField(max_length=350, verbose_name='Описание')
    img = models.ImageField(verbose_name='Изображение') 

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'этап'
        verbose_name_plural = 'Этапы работ'

class Settings(models.Model):
    number = models.CharField(max_length=17, verbose_name='Номер телефона')
    alt_number = models.CharField(max_length=17, verbose_name='Дополнительный номер телефона')
    address = models.CharField(max_length=500, verbose_name='Адресс офиса')
    email = models.EmailField(verbose_name='Адресс электронной почты')
    vk_url = models.URLField(max_length=500, verbose_name='Ссылка на группу VK')
    instagram_url = models.URLField(max_length=500, verbose_name='Ссылка на Instagram')
    twitter_url = models.URLField(max_length=500, verbose_name='Ссылка на Twitter')
    fb_url = models.URLField(max_length=500, verbose_name='Ссылка на группу Facebook')
    about_descript = models.TextField(verbose_name='Описание')
    year_of_foundation = models.IntegerField(verbose_name='Год основания')
    designers = models.IntegerField(verbose_name='Дизайнеров в команде')
    contractors = models.IntegerField(verbose_name='Количество постоянных подрядчиков')
    active = models.BooleanField(default=False, verbose_name='Активность профиля')

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'Основные настройки'
