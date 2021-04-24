from django.db import models
from django.utils import timezone


class Survey(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    start_date = models.DateTimeField(verbose_name="Дата старта", default=timezone.now)
    finish_date = models.DateTimeField(verbose_name="Дата окончания")
    description = models.TextField(verbose_name="Описание", default='', blank=True)


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст", default='', blank=True)
    TEXT_TYPE = 'TT'
    ONE_OPTION = 'OO'
    MULTIPLE_OPTIONS = 'MO'
    TYPE_CHOICES = [
        (TEXT_TYPE, 'Текстом'),
        (ONE_OPTION, 'С выбором одного варианта'),
        (MULTIPLE_OPTIONS, 'С выбором нескольких вариантов'),
    ]
    question_type = models.CharField(
        verbose_name="Тип вопроса",
        max_length=2,
        choices=TYPE_CHOICES,
        default=TEXT_TYPE,
    )


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст")


class Answer(models.Model):
    responder_id = models.IntegerField(verbose_name="ID респондента")
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст", default='', blank=True)
