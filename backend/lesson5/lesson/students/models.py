# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
# pylint: disable=missing-class-docstring
# pylint: disable=trailing-whitespace
# from tokenize import group
from django.db import models

# Create your models here.
class Subject(models.Model):

    name = models.CharField(verbose_name="Предмет",
                            max_length=100,
                            blank=True,
                            null=True)
    
    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        #self.name += '111'
        super().save(*args, **kwargs)
        #self.name += '55555555'

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

class StudentGroup(models.Model):
    name = models.CharField(verbose_name="Имя Группы", max_length=100)
    students_number = models.DecimalField(max_digits=4, decimal_places=0,
                                            verbose_name="Кол-во студентов",
                                            blank=True,
                                            null=True)
    subjects = models.ForeignKey(Subject, verbose_name="Предмет",
                                    on_delete=models.CASCADE,
                                    null=True,
                                    related_name="subjects",
                                    blank=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Группа студентов"
        verbose_name_plural = "Группы студентов"


class Student(models.Model):

    SURNAME_CHOICES = (
        ('Petrenko', 'Петренко'),
        ('Ivanenko', 'Іваненко'),
    )

    name = models.CharField(verbose_name="Имя",
                            max_length=100,
                            blank=True,
                            null=True)
    surname = models.CharField(verbose_name="Фамилия",
                            max_length=100,
                            blank=True,
                            null=True,
                            choices=SURNAME_CHOICES)
    birthday = models.DateField(verbose_name="День рождения",
                                null=True,
                                blank=True)
    group = models.ForeignKey(StudentGroup, verbose_name="Группа N",
                                    on_delete=models.CASCADE,
                                    null=True,
                                    related_name="students",
                                    blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        #self.name += '111'
        super().save(*args, **kwargs)
        #self.name += '55555555'

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

