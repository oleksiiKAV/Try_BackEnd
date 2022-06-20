# Generated by Django 4.0.5 on 2022-06-20 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_studentgroup_student_birthday_student_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AlterModelOptions(
            name='studentgroup',
            options={'verbose_name': 'Группа студентов', 'verbose_name_plural': 'Группы студентов'},
        ),
        migrations.AddField(
            model_name='student',
            name='surname',
            field=models.CharField(blank=True, choices=[('Petrenko', 'Петренко'), ('Ivanenko', 'Іваненко')], max_length=100, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='students_number',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True, verbose_name='Кол-во студентов'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.studentgroup', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
    ]
