from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='banners/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    
class Services(models.Model):
    title = models.CharField(max_length=300)
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Ideas(models.Model):
    title = models.CharField(max_length=300)
    percent = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'


class Feedback(models.Model):
    CHANNELS = (
        ('call', 'звонок'),
        ('message', 'сообщения'),
        ('email', 'почта')
    )

    name = models.CharField(max_length=50)
    channel = models.CharField(max_length=25, choices=CHANNELS)
    image = models.ImageField(upload_to='authors/')
    comment = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class CallBack(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'


class Subscribtion(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
