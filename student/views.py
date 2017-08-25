from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from teacher.models import *
from student.models import *
from quiz.models import *
from django.forms.formsets import formset_factory
from .forms import ShortAnswerForm, MultiChoiceForm, OneChoiceForm
from django.utils.functional import curry
from django.utils import timezone


# Create your views here.
def student_quiz(request, Subject_Order):

    username = request.user.username
    #submitAssigns = SubmitAssign.objects.filter(assignNum= Subject_Order)
    submitAssigns = SubmitAssign.objects.filter(studentID__username = username).filter(assignNum__subjectNum = Subject_Order)
#    assignments = Assignment.objects.filter(subjectNum = Subject_Order)
    return render(request, 'student/student_quiz.html', {'submitassigns':submitAssigns})

def student_subject(request):

    username = request.user.username
    subjectMember = SubjectMember.objects.filter(person__user__username=username)
    return render(request, 'student/student_subject.html', {'subjectMember':subjectMember})


def student_take_quiz(request, Quiz_Order):

    takequizshorts = quiz_short.objects.filter(AssignNum = Quiz_Order)
    takequizones = quiz_one.objects.filter(AssignNum = Quiz_Order)
    takequizmultis = quiz_multi.objects.filter(AssignNum = Quiz_Order)

    my_iterator_short = takequizshorts.iterator()
    FormSet_Short_Answer_Forms = formset_factory(ShortAnswerForm, extra=len(takequizshorts))
    try:
        FormSet_Short_Answer_Forms.form = staticmethod(curry(ShortAnswerForm, item_iterator_short=my_iterator_short))
    except:
        pass

    my_iterator = takequizones.iterator()
    FormSet_One_Answer_Forms = formset_factory(OneChoiceForm, extra=len(takequizones))
    try:
        FormSet_One_Answer_Forms.form = staticmethod(curry(OneChoiceForm, item_iterator=my_iterator))
    except:
        pass

    my_iterator_multi = takequizmultis.iterator()
    FormSet_Multi_Answer_Forms = formset_factory(MultiChoiceForm, extra=len(takequizmultis))
    try:
        FormSet_Multi_Answer_Forms.form = staticmethod(curry(MultiChoiceForm, item_iterator_multi=my_iterator_multi))
    except:
        pass

    if request.method == 'POST':
        formset_short_answer_forms = FormSet_Short_Answer_Forms(request.POST, prefix="short_answer_forms")
        formset_one_answer_forms = FormSet_One_Answer_Forms(request.POST, prefix="one_answer_forms")
        formset_multi_answer_forms = FormSet_Multi_Answer_Forms(request.POST, prefix="multi_answer_forms")
        print(request.POST)

        grade = 0
        correct = 0
        wrong = 0

        if formset_short_answer_forms.is_valid() and formset_one_answer_forms.is_valid() and formset_multi_answer_forms.is_valid():
            for f in formset_short_answer_forms:
                cd = f.cleaned_data
                answer = cd.get('answer')


                f.correct_short = f.quiz_short.Answer == answer

                if f.correct_short :
                    grade = grade + 1
                    correct = correct + 1
                else :
                    wrong = wrong + 1

            for f in formset_one_answer_forms:
                cd = f.cleaned_data
                answer_key = cd.get('one_answer')


                f.correct_one_check = f.quiz_one.Check == answer_key
                if f.correct_one_check:
                    grade = grade + 1
                    correct = correct + 1
                else :
                    wrong = wrong + 1



            for f in formset_multi_answer_forms:
                cd = f.cleaned_data
                answer_list = cd.get('multi_answer')

                correct_list = []
                if f.quiz_multi.Check_1 == True:
                    correct_list.append('a_multi')
                if f.quiz_multi.Check_2 == True:
                    correct_list.append('b_multi')
                if f.quiz_multi.Check_3 == True:
                    correct_list.append('c_multi')
                if f.quiz_multi.Check_4 == True:
                    correct_list.append('d_multi')

                f.correct_multi_check = correct_list == answer_list
                if f.correct_multi_check :
                    grade = grade + 1
                    correct = correct + 1
                else :
                    wrong = wrong + 1

            total=correct+wrong
            print(total)
            print(correct)
            print(wrong)

            assignment = Assignment.objects.get(assignNum=Quiz_Order)
            submitassign = SubmitAssign.objects.filter(assignNum = assignment, studentID = request.user)
            submitassign.update(grade = grade, submitTime=timezone.now())

#            context =  {'takequizshorts':takequizshorts, 'takequizones':takequizones, 'takequizmultis':takequizmultis, 'formsetshortanswerforms':formset_short_answer_forms, 'formsetoneanswerforms':formset_one_answer_forms, 'formsetmultianswerforms':formset_multi_answer_forms}
#            return HttpResponseRedirect('student_quiz_result.html', context)

            context =  {'total':total, 'correct':correct, 'wrong':wrong, 'takequizshorts':takequizshorts, 'takequizones':takequizones, 'takequizmultis':takequizmultis, 'formsetshortanswerforms':formset_short_answer_forms, 'formsetoneanswerforms':formset_one_answer_forms, 'formsetmultianswerforms':formset_multi_answer_forms}
            return render(request, 'student/student_quiz_result.html', context)
    else:
        formset_short_answer_forms = FormSet_Short_Answer_Forms(prefix="short_answer_forms")
        formset_one_answer_forms = FormSet_One_Answer_Forms(prefix="one_answer_forms")
        formset_multi_answer_forms = FormSet_Multi_Answer_Forms(prefix="multi_answer_forms")

    context =  {'takequizshorts':takequizshorts, 'takequizones':takequizones, 'takequizmultis':takequizmultis, 'formsetshortanswerforms':formset_short_answer_forms, 'formsetoneanswerforms':formset_one_answer_forms, 'formsetmultianswerforms':formset_multi_answer_forms}
    return render(request, 'student/student_take_quiz.html', context)
