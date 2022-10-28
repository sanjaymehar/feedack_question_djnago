from django.db import models

# Create your models here.

number=(('5','5'),('10','10'))    
answer_type=(('text','text'),('feedback','feedback'))


class Question(models.Model):
    question=models.CharField(max_length=40)
    typee = models.CharField(max_length=10, choices=answer_type)
    rating=models.CharField(max_length = 10,choices = number,blank=True)

    def __str__(self):
        return self.question
class sesion(models.Model):
    sid=models.CharField(max_length=200)

class Feedbacks(models.Model):
    sid=models.ForeignKey(sesion,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    text=models.CharField(max_length=40,blank=True)
    num=models.IntegerField(blank=True, null=True)

  
