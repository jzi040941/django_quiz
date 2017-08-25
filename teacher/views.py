from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from student.models import SubmitAssign
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from mysite.settings import BASE_DIR
import os
#teacher

def teacher_quiz(request,subject_Num):

    #Subject = get_object_or_404(Subject, subjectNum=subjectNum)
    assignments = Assignment.objects.filter(subjectNum = subject_Num)
    #assignments = Assignment.objects.get(subjectNum=subject_Num)
    return render(request, 'teacher/teacher_quiz.html', {'assignments':assignments, 'subjectNum':subject_Num})

def teacher_subject(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        subjects = Subject.objects.filter(professor__username=username)
        return render(request, 'teacher/teacher_subject.html', {'subjects':subjects, 'username':username})
    else:
        return redirect("/accounts/login")
def formset_save(formset,assignment):
    for form in formset:
        if form.has_changed():
            quiz_instance = form.save(commit=False)
            quiz_instance.AssignNum = assignment
            quiz_instance.save()
def quiz_new(request,subject_Num):

    Quiz_shortFormSet = formset_factory(Quiz_shortForm)
    Quiz_oneFormSet = formset_factory(Quiz_oneForm)
    Quiz_multiFormSet = formset_factory(Quiz_multiForm)
    if request.method == "POST":
        assignmentform = AssignmentForm(request.POST,prefix="assignmnetform")
        quiz_shortformset = Quiz_shortFormSet(request.POST,prefix="quiz_shortform")
        quiz_oneformset = Quiz_oneFormSet(request.POST,prefix="quiz_oneform")
        quiz_multiformset = Quiz_multiFormSet(request.POST,prefix="quiz_multiform")
        print(request.POST)
        if assignmentform.is_valid():
            assignment = assignmentform.save(commit=False)
            assignment.published_date = timezone.now()
            assignment.subjectNum = Subject.objects.get(subjectNum=subject_Num)
            assignment.save()
            if quiz_shortformset.is_valid() and quiz_oneformset.is_valid() and quiz_multiformset.is_valid():
                formset_save(quiz_shortformset,assignment)
                formset_save(quiz_oneformset,assignment)
                formset_save(quiz_multiformset,assignment)
            #redirect change need
                return redirect("/teacher")
            else:
                print (quiz_shortformset.errors)
                print (quiz_oneformset.errors)
                print (quiz_multiformset.errors)
                return redirect("/error")
    else:
        assignmentform = AssignmentForm(prefix="assignmnetform")
        quiz_shortFormSet = Quiz_shortFormSet(prefix="quiz_shortform")
        quiz_oneFormSet = Quiz_oneFormSet(prefix="quiz_oneform")
        quiz_multiFormSet = Quiz_multiFormSet(prefix="quiz_multiform")

    context = {'assignmentForm' : assignmentform,
            'quiz_shortformset' : quiz_shortFormSet,
                'quiz_oneformset' : quiz_oneFormSet,
                'quiz_multiformset' : quiz_multiFormSet}
    return render(request, 'teacher/quiz_edit.html',context )

def quiz_modify(request, assign_Num):
    Quiz_shortFormSet = modelformset_factory(quiz_short, form = Quiz_shortForm)
    Quiz_oneFormSet = modelformset_factory(quiz_one, form = Quiz_oneForm)
    Quiz_multiFormSet = modelformset_factory(quiz_multi, form = Quiz_multiForm)

    assignment = Assignment.objects.get(assignNum = assign_Num)
    quiz_shortQueryset = quiz_short.objects.filter(AssignNum = assignment)
    quiz_oneQueryset = quiz_one.objects.filter(AssignNum = assignment)
    quiz_multiQueryset = quiz_multi.objects.filter(AssignNum = assignment)
    if request.method == "POST":
        assignmentform = AssignmentForm(request.POST,prefix="assignmnetform",instance=assignment)
        quiz_shortformset = Quiz_shortFormSet(request.POST,prefix="quiz_shortform", queryset=quiz_shortQueryset)
        quiz_oneformset = Quiz_oneFormSet(request.POST,prefix="quiz_oneform", queryset=quiz_oneQueryset)
        quiz_multiformset = Quiz_multiFormSet(request.POST,prefix="quiz_multiform", queryset=quiz_multiQueryset)
        print(request.POST)
        if assignmentform.is_valid():
            saved_assignment = assignmentform.save(commit=False)
            saved_assignment.published_date = timezone.now()
            saved_assignment.subjectNum = assignment.subjectNum
            saved_assignment.save()
            if quiz_shortformset.is_valid() and quiz_oneformset.is_valid() and quiz_multiformset.is_valid():
                formset_save(quiz_shortformset,saved_assignment)
                formset_save(quiz_oneformset,saved_assignment)
                formset_save(quiz_multiformset,saved_assignment)
            #redirect change need
                return redirect("/teacher")
            else:
                print (quiz_multiformset.errors)
                return redirect("/error")
    else:

        assignmentform = AssignmentForm(instance=assignment, prefix="assignmnetform")
        quiz_shortFormSet = Quiz_shortFormSet(queryset=quiz_shortQueryset, prefix="quiz_shortform")
        quiz_oneFormSet = Quiz_oneFormSet(queryset=quiz_oneQueryset, prefix="quiz_oneform")
        quiz_multiFormSet = Quiz_multiFormSet(queryset=quiz_multiQueryset, prefix="quiz_multiform")

    context = {'assignmentForm' : assignmentform,
            'quiz_shortformset' : quiz_shortFormSet,
                'quiz_oneformset' : quiz_oneFormSet,
                'quiz_multiformset' : quiz_multiFormSet}
    return render(request, 'teacher/quiz_edit.html',context )

def quiz_submit_check(request,assign_Num):
    context = {'assign_Num' : assign_Num}
    assignment = Assignment.objects.get(assignNum = assign_Num)
    submitassigns = SubmitAssign.objects.filter(assignNum = assignment).order_by('studentID','submittime').distinct('studentID')
    subjectNum = assignment.subjectNum.subjectNum
    return render(request, 'teacher/quiz_submit_check.html',context )

'''
def teacher_thank_you(request):
    return render(request, 'teacher/teacher_thank_you.html')
'''
