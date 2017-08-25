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
import random
from datetime import datetime, timedelta
from .views import student_quiz
def student_take_quiz(request, Quiz_Order):
    assignment = Assignment.objects.get(assignNum=Quiz_Order)
    submitassign = SubmitAssign.objects.get(assignNum = assignment, studentID = request.user)

    '''
    #check if submittime is before 5hours
    if timezone.now() - submitassign.submitTime < timedelta(hours=5):
        #submitAssigns = SubmitAssign.objects.filter(studentID__username = request.user.username).filter(assignNum__subjectNum = assignment.subjectNum.subjectNum)
        #return render(request, 'student/student_quiz.html', {'submitassigns':submitAssigns})
        return student_quiz(request, assignment.subjectNum.subjectNum)
    '''
    if assignment.amountQuizShort is None :
        takequizshorts = quiz_short.objects.filter(AssignNum = Quiz_Order)
    else:
        quiz_id_list = quiz_shortManager.objects.filter(submitAssign = submitassign).values_list('quiz',flat=True)
        if len(quiz_id_list)==0 :
            id_list = quiz_short.objects.filter(AssignNum = Quiz_Order).values_list('id', flat=True)
            random_id_list = random.sample(list(id_list), min(len(list(id_list)),assignment.amountQuizShort))
            #takequizshorts = quiz_short.objects.filter(id__in=random_id_list)
            for quiz_id in random_id_list:
                quiz_shortManager.objects.create(submitAssign=submitassign,quiz_id=quiz_id)
            quiz_id_list = quiz_shortManager.objects.filter(submitAssign = submitassign).values_list('quiz',flat=True)
            takequizshorts = quiz_short.objects.filter(id__in=quiz_id_list)
        else:
            takequizshorts = quiz_short.objects.filter(id__in=quiz_id_list)

    if assignment.amountQuizOne is None :
        takequizones = quiz_one.objects.filter(AssignNum = Quiz_Order)
    else:
        quiz_id_list = quiz_oneManager.objects.filter(submitAssign = submitassign).values_list('quiz',flat=True)
        if len(quiz_id_list)==0 :
            id_list = quiz_one.objects.filter(AssignNum = Quiz_Order).values_list('id', flat=True)
            random_id_list = random.sample(list(id_list), min(len(list(id_list)),assignment.amountQuizOne))
            #takequizones = quiz_one.objects.filter(id__in=random_id_list)
            for quiz_id in random_id_list:
                quiz_oneManager.objects.create(submitAssign=submitassign,quiz_id=quiz_id)
            quiz_id_list = quiz_oneManager.objects.filter(submitAssign = submitassign).values_list('quiz',flat=True)
            takequizones = quiz_one.objects.filter(id__in=quiz_id_list)
        else:
            takequizones = quiz_one.objects.filter(id__in=quiz_id_list)

    if assignment.amountQuizMulti is None :
        takequizmultis = quiz_multi.objects.filter(AssignNum = Quiz_Order)
    else:
        quiz_id_list = quiz_multiManager.objects.filter(submitAssign = submitassign).values_list('quiz',flat=True)
        if len(quiz_id_list)==0 :
            id_list = quiz_multi.objects.filter(AssignNum = Quiz_Order).values_list('id', flat=True)
            random_id_list = random.sample(list(id_list), min(len(list(id_list)),assignment.amountQuizMulti))
            #takequizmultis = quiz_multi.objects.filter(id__in=random_id_list)
            for quiz_id in random_id_list:
                quiz_multiManager.objects.create(submitAssign=submitassign,quiz_id=quiz_id)
            quiz_id_list = quiz_multiManager.objects.filter(submitAssign = submitassign).values_list('quiz',flat=True)
            takequizmultis = quiz_multi.objects.filter(id__in=quiz_id_list)
        else:
            takequizmultis = quiz_multi.objects.filter(id__in=quiz_id_list)

    #takequizones = quiz_one.objects.filter(AssignNum = Quiz_Order)
    #takequizmultis = quiz_multi.objects.filter(AssignNum = Quiz_Order)

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

        if formset_short_answer_forms.is_valid() and formset_one_answer_forms.is_valid() and formset_multi_answer_forms.is_valid():
            for f in formset_short_answer_forms:
                cd = f.cleaned_data
                answer = cd.get('answer')

                '''
                short_answer_result[sar]=f.quiz_short.Answer
                print(short_answer_result[sar])
                '''
                f.correct_short = f.quiz_short.Answer == answer

                if f.correct_short :
                    grade = grade + 1

            for f in formset_one_answer_forms:
                cd = f.cleaned_data
                answer_key = cd.get('one_answer')
                '''
                print(dict(f.fields['one_answer'].choices).get(answer_key))
                #if f.quiz_one.Answer == one_answer :
                if f.quiz_one.Answer == dict(f.fields['one_answer'].choices).get(answer_key):
                    grade = grade + 1
                '''

                f.correct_one_check = f.quiz_one.Check == answer_key
                if f.correct_one_check:
                    grade = grade + 1

                '''
                correct_list_multi = []
                if f.quiz_one.Check_1 == True:
                    correct_list_multi.append('1')
                if f.quiz_one.Check_2 == True:
                    correct_list_multi.append('2')
                if f.quiz_one.Check_3 == True:
                    correct_list_multi.append('3')
                if f.quiz_one.Check_4 == True:
                    correct_list_multi.append('4')

                if correct_list_multi == answer_list_multi :
                    grade = grade + 1
                '''

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
            assignment = Assignment.objects.get(assignNum=Quiz_Order)
            submitassign = SubmitAssign.objects.filter(assignNum = assignment, studentID = request.user)
            submitassign.update(grade = grade, submitTime=timezone.now())

            quiz_oneManager.objects.filter(submitAssign = submitassign).delete()
            quiz_multiManager.objects.filter(submitAssign = submitassign).delete()
            quiz_shortManager.objects.filter(submitAssign = submitassign).delete()
#            context =  {'takequizshorts':takequizshorts, 'takequizones':takequizones, 'takequizmultis':takequizmultis, 'formsetshortanswerforms':formset_short_answer_forms, 'formsetoneanswerforms':formset_one_answer_forms, 'formsetmultianswerforms':formset_multi_answer_forms}
#            return HttpResponseRedirect('student_quiz_result.html', context)

            questionquantity = len(takequizshorts) + len(takequizones) + len(takequizmultis)
            context =  {'takequizshorts':takequizshorts, 'takequizones':takequizones, 'takequizmultis':takequizmultis, 'formsetshortanswerforms':formset_short_answer_forms, 'formsetoneanswerforms':formset_one_answer_forms, 'formsetmultianswerforms':formset_multi_answer_forms,
                        'grade':grade,
                        'questionquantity':questionquantity}
            return render(request, 'student/student_quiz_result.html', context)
    else:
        formset_short_answer_forms = FormSet_Short_Answer_Forms(prefix="short_answer_forms")
        formset_one_answer_forms = FormSet_One_Answer_Forms(prefix="one_answer_forms")
        formset_multi_answer_forms = FormSet_Multi_Answer_Forms(prefix="multi_answer_forms")

    context =  {'takequizshorts':takequizshorts, 'takequizones':takequizones, 'takequizmultis':takequizmultis, 'formsetshortanswerforms':formset_short_answer_forms, 'formsetoneanswerforms':formset_one_answer_forms, 'formsetmultianswerforms':formset_multi_answer_forms}
    return render(request, 'student/student_take_quiz.html', context)
