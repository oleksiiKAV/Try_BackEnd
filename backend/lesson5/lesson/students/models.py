from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    #birthday = models.DateField(verbose_name="Birthday Day", blank=True, null=True)
    #group = models.ForeignKey(StudentGroup,verbose_name="Group of Student", max_length=100, blank=True, null=True)
    
    def __str__(self):
        return (str(self.name))

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
