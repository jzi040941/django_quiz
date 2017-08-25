from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from quiz.models import *
from teacher.models import Assignment

# Create your models here.
class SubmitAssign(models.Model):
    assignNum = models.ForeignKey('teacher.Assignment',on_delete=models.CASCADE,)
    studentID = models.ForeignKey('auth.User')
    grade = models.CharField(max_length=100, default='No Grade') #일케 해도 괜찮?
    submitTime = models.DateTimeField(null = True)
    quiz_oneIds = models.ManyToManyField('quiz.quiz_one', through='quiz_oneManager')
    quiz_multiIds = models.ManyToManyField('quiz.quiz_multi', through='quiz_multiManager')
    quiz_shortIds = models.ManyToManyField('quiz.quiz_short', through='quiz_shortManager')
#    def __init__(self, assignment, student):
#        self.assignNum = assignment.assignNupm
#        self.assignName = assignment.assignName
#        self.studentID = student.username
#        grade = 0
    class Meta:
        unique_together = (("assignNum", "studentID"),)
    def set_grade(self, grade):
        #grade = models.ForeignKey #여기 채워야함(다른 곳에서 받아와야함)
        self.grade = grade/100*30
        self.save()

    #def show_result(채점되어 있는 시험지 보여주기?)

    def __str__(self):
        return "%s assignment submiited by %s" % (self.assignNum.assignName, self.studentID.username)

class quiz_oneManager(models.Model):
    submitAssign = models.ForeignKey('submitAssign')
    quiz = models.ForeignKey('quiz.quiz_one')

class quiz_shortManager(models.Model):
    submitAssign = models.ForeignKey('submitAssign')
    quiz = models.ForeignKey('quiz.quiz_short')

class quiz_multiManager(models.Model):
    submitAssign = models.ForeignKey('submitAssign')
    quiz = models.ForeignKey('quiz.quiz_multi')

@receiver(post_save, sender=Assignment)
def create_submitassign_by_assignment(sender, instance, created, **kwargs):
    if created:
        subjectmembers = SubjectMember.objects.filter(subject=instance.subjectNum)
        for subjectmember in subjectmembers:
            SubmitAssign.objects.create(assignNum = instance, studentID = subjectmember.person.user, submitTime=None)

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    subjects = models.ManyToManyField('teacher.Subject', through='SubjectMember', related_name='people')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_UserProfile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class SubjectMember(models.Model):
    person = models.ForeignKey('UserProfile')
    #, related_name='membership')
    subject = models.ForeignKey('teacher.Subject')
    #, related_name='membership')
    type = models.CharField(max_length=100)

    def __str__(self):
        return "%s is in subject %s (as %s)" % (self.person, self.subject, self.type)

@receiver(post_save, sender=SubjectMember)
def create_submitassign(sender, instance, created, **kwargs):
    if created:
        assignments = Assignment.objects.filter(subjectNum=instance.subject)
        for assignment in assignments:
            SubmitAssign.objects.create(studentID = instance.person.user, submittime=None, assignNum=assignment)
'''
class answer_short(models.Model):
    #AssignNum = models.ForeignKey('quiz.quiz_short', related_name='AssignNum')
    Question = models.ForeignKey('quiz.quiz_short')
'''
