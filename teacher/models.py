from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
#import #여기 채워야함(학생정보 있는 DB)
#import #여기 채워야함(학생이 제출한 과제답이 있는 DB-점수)


class Subject(models.Model):
    subjectNum = models.CharField(primary_key=True,max_length=255)
    subjectName = models.CharField(max_length=128)
    professor = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL)
    classroom = models.CharField(max_length=128)
    classtime = models.DateTimeField() #수업시간에 대한 정보를 알아야함

    def __str__(self):
        return self.subjectName

class Assignment(models.Model):
    assignNum = models.AutoField(primary_key=True)
    #assignNum = models.CharField(
    #    max_length=20, primary_key=True)
    assignName = models.CharField(max_length=30)
    subjectNum = models.ForeignKey('Subject', on_delete=models.CASCADE)
    published_date = models.DateTimeField(
            blank=True, null=True)
    amountQuizShort = models.IntegerField(null=True)
    amountQuizOne = models.IntegerField(null=True)
    amountQuizMulti = models.IntegerField(null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.assignName
