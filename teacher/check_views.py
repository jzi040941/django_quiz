from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from student.models import SubmitAssign
from .tables import SubmitAssignTable
from django_tables2 import RequestConfig

def quiz_submit_check(request,assign_Num):

    assignment = Assignment.objects.get(assignNum = assign_Num)
    submitassigns = SubmitAssign.objects.filter(assignNum = assignment).order_by('studentID')
    table = SubmitAssignTable(submitassigns)
    RequestConfig(request).configure(table)
    subjectNum = assignment.subjectNum.subjectNum
    context = {'assign_Num' : assign_Num, 'table' : table}
    print(submitassigns)
    return render(request, 'teacher/quiz_submit_check.html',context )
