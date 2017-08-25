from django.db import models

# Create your models here.
class quiz_short(models.Model):
    AssignNum = models.ForeignKey('teacher.Assignment', on_delete=models.CASCADE)
    Question = models.TextField()
    Answer = models.TextField()

    def __str__(self):
        return "AssignNum : %s, question: %s Answer: %s" % (self.AssignNum, self.Question, self.Answer)

class quiz_one(models.Model):
    AssignNum = models.ForeignKey('teacher.Assignment', on_delete=models.CASCADE)
    Question = models.TextField()
#   Check = models.CharField(max_length=7, choices=CHECK_LIST)
    Check = models.IntegerField(null=True,blank=True)

    '''
    Check_1 = models.BooleanField()
    Check_2 = models.BooleanField()
    Check_3 = models.BooleanField()
    Check_4 = models.BooleanField()
    '''
    Selection_1 = models.TextField()
    Selection_2 = models.TextField()
    Selection_3 = models.TextField()
    Selection_4 = models.TextField()

    def __str__(self):
        return "AssignNum : %s, question: %s Selection_1: %s" % (self.AssignNum, self.Question, self.Selection_1)

'''
class quiz_one(models.Model):
    AssignNum = models.ForeignKey('teacher.Assignment', on_delete=models.CASCADE)
    Question = models.TextField()
    Answer = models.TextField()
    Wrong_1 = models.TextField()
    Wrong_2 = models.TextField()
    Wrong_3 = models.TextField()

    def __str__(self):
        return "AssignNum : %s, question: %s Answer: %s" % (self.AssignNum, self.Question, self.Answer)
'''
class quiz_multi(models.Model):
    AssignNum = models.ForeignKey('teacher.Assignment', on_delete=models.CASCADE)
    Question = models.TextField()
    Check_1 = models.BooleanField()
    Check_2 = models.BooleanField()
    Check_3 = models.BooleanField()
    Check_4 = models.BooleanField()
    Selection_1 = models.TextField()
    Selection_2 = models.TextField()
    Selection_3 = models.TextField()
    Selection_4 = models.TextField()

    def __str__(self):
        return "AssignNum : %s, question: %s Selection_1: %s" % (self.AssignNum, self.Question, self.Selection_1)
