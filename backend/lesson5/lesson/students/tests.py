from unicodedata import name
from django.test import TestCase

# Create your tests here.
from .models import Student,StudentGroup,Subject

class StudentModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Student.objects.create(name='Big', surname='Bob', birthday='2001-12-12')

    def test_first_name_label(self):
        stud=Student.objects.get(id=1)
        field_label = stud._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Имя')

    def test_date_of_death_label(self):
        stud=Student.objects.get(id=1)
        field_label = stud._meta.get_field('birthday').verbose_name
        self.assertEquals(field_label,'День рождения')

    def test_first_name_max_length(self):
        stud=Student.objects.get(id=1)
        max_length = stud._meta.get_field('name').max_length
        self.assertEquals(max_length,100)

    # def test_object_name_is_last_name_comma_first_name(self):
    #     author=Author.objects.get(id=1)
    #     expected_object_name = '%s, %s' % (author.last_name, author.first_name)
    #     self.assertEquals(expected_object_name,str(author))

    # def test_get_absolute_url(self):
    #     author=Author.objects.get(id=1)
    #     #This will also fail if the urlconf is not defined.
    #     self.assertEquals(author.get_absolute_url(),'/catalog/author/1')