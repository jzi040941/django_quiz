from django import forms
from quiz.models import *
class ShortAnswerForm(forms.Form):
    #answer = forms.CharField(label='short_answer', max_length=100)

    answer = forms.CharField(required=False, max_length=100)
    quiz_short = 0
    def __init__(self, *args, **kwargs):
        self.quiz_short = next(kwargs.pop('item_iterator_short'))
        super(ShortAnswerForm, self).__init__(*args, **kwargs)
        self.fields['answer'] = forms.CharField(label=self.quiz_short.Question, required=False, max_length=100)
        self.fields['answer'].widget.attrs['class'] = 'form-control'
#class answer_one(forms.Form):
'''
answer_choices_one = (('a_one','a.'),('b_one','b.'),('c_one','c'),('d_one','d'))
class OneChoiceForm(forms.Form):
    one_answer = forms.MultipleChoiceField(label='one_answer', required=False, widget=forms.RadioSelect, choices=answer_choices_one)
'''

def get_one_choice(answer):
    choices_list =((1, answer.Selection_1), (2, answer.Selection_2), (3, answer.Selection_3), (4, answer.Selection_4))
    #   choices_list ={1:answer.Answer, 2:, answer.Wrong_1), ('3', answer.Wrong_2), ('4', answer.Wrong_3))}
    #choices_list =(('a_one', '1'), ('b_one', '2'), ('c_one', 'answer.Wrong_2'), ('d_one',' answer.Wrong_3'))
    return choices_list

class OneChoiceForm(forms.Form):
    one_answer =  forms.TypedChoiceField(required=False, widget=forms.RadioSelect, coerce=int)
    def __init__(self, *args, **kwargs):
        self.quiz_one = next(kwargs.pop('item_iterator'))
        super(OneChoiceForm, self).__init__(*args, **kwargs)
        self.fields['one_answer'] = forms.TypedChoiceField(label=self.quiz_one.Question, required=False, widget=forms.RadioSelect(attrs={"class":""}), choices=get_one_choice(self.quiz_one), coerce=int)

'''
def get_one_choice(answer):

    A = answer.Answer
    Wrong_1 = answer.Wrong_1
    Wrong_2 = answer.Wrong_2
    Wrong_3 = answer.Wrong_3

    choices_list =(('1', answer.Answer), ('2', answer.Wrong_1), ('3', answer.Wrong_2), ('4', answer.Wrong_3))
    #   choices_list ={1:answer.Answer, 2:, answer.Wrong_1), ('3', answer.Wrong_2), ('4', answer.Wrong_3))}
    #choices_list =(('a_one', '1'), ('b_one', '2'), ('c_one', 'answer.Wrong_2'), ('d_one',' answer.Wrong_3'))
    return choices_list

class OneChoiceForm(forms.Form):
    one_answer =  forms.ChoiceField(required=False, widget=forms.RadioSelect)
    def __init__(self, *args, **kwargs):
        self.quiz_one = next(kwargs.pop('item_iterator'))
        super(OneChoiceForm, self).__init__(*args, **kwargs)
        self.fields['one_answer'] = forms.ChoiceField(label=self.quiz_one.Question, required=False, widget=forms.RadioSelect, choices=get_one_choice(self.quiz_one))
'''

def get_multi_choice(answer):
    choices_list =(('a_multi', answer.Selection_1), ('b_multi', answer.Selection_2), ('c_multi', answer.Selection_3), ('d_multi', answer.Selection_4))
    return choices_list

class MultiChoiceForm(forms.Form):
    multi_answer = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple)
    def __init__(self, *args, **kwargs):
        self.quiz_multi = next(kwargs.pop('item_iterator_multi'))
        super(MultiChoiceForm, self).__init__(*args, **kwargs)
        self.fields['multi_answer'] = forms.MultipleChoiceField(label=self.quiz_multi.Question, required=False, widget=forms.CheckboxSelectMultiple, choices=get_multi_choice(self.quiz_multi))

'''
answer_choices_multi = (('a_multi','a.'),('b_multi','b.'),('c_multi','c.'),('d_multi','d.'))

class MultiChoiceForm(forms.Form):
    answers = forms.MultipleChoiceField(label='multi_answer', required=False, widget=forms.CheckboxSelectMultiple, choices=answer_choices_multi)
'''
#class answer_multi(forms.Form):
