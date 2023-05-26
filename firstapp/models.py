from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="blog/images",
                              verbose_name="Изображение")
    date = models.DateField(default=datetime.date.today,
verbose_name="Дата")
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"

class ListGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    name = models.CharField(max_length=250, verbose_name="Заголовок группы")
    description = models.TextField(
        max_length=5000, blank=True, verbose_name="Описание группы")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Список групп'
        verbose_name_plural = 'Список групп'

class UserProfileInfo(models.Model):
     
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    Standard = models.ForeignKey(ListGroups, on_delete=models.CASCADE,verbose_name="Название группы",null=True, blank=True)
    direction = models.CharField(max_length=500, verbose_name="Направление", blank=True)
    education = models.CharField(max_length=500, verbose_name="Образование", blank=True)  
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")
    experience = models.PositiveSmallIntegerField(max_length=500, verbose_name="Стаж(в месяцах)", blank=True)
    place_education  = models.TextField(max_length=500, blank=True,verbose_name='Место учёбы')
    atchievments = models.TextField(max_length=500, blank=True,verbose_name='Достижения')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Информация о пользователях'
        verbose_name_plural = 'Информация о пользователях'

CHOICES = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
        
    )

class ListStudents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    groups = models.ManyToManyField(ListGroups,verbose_name='Группы')
    fio = models.CharField(max_length=250, verbose_name="Фио ребенка")
    age = models.PositiveSmallIntegerField(
         blank=True, verbose_name="Возраст ребёнка")
    birsday = models.DateField(verbose_name="Дата рождения ребёнка")
    pol = models.CharField(max_length=300, choices = CHOICES,verbose_name='пол ребенка')
    place_learning = models.CharField(max_length=250, verbose_name="Место обучения ребёнка") 
    sertificat_pfdo = models.PositiveIntegerField(max_length=250, verbose_name="Cертификат ПФДО рёбенка")
    fio_parents  = models.TextField(max_length=500, blank=True,verbose_name='ФИО родителей')
    contact_data = models.PositiveIntegerField(max_length=250, verbose_name="Контактные данные")
    atchievments = models.TextField(max_length=500, blank=True,verbose_name='Достижения')
    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'Список студентов'
        verbose_name_plural = 'Список студентов'
 