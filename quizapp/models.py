from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class questions(models.Model):
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000)
    option4 = models.CharField(max_length=1000)
    category = models.ForeignKey(category, on_delete=models.CASCADE) 
    answer_option = [('a', 'option1'),('b', 'option2'),('c', 'option3'),('d', 'option4')]
    answer = models.CharField(max_length=100 , choices = answer_option, default='none')
    
    def __str__(self):
        return self.category.name