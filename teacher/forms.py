from django.forms import Textarea,TextInput
from django import forms
from .models import *
from quiz.models import *
from django.forms.formsets import BaseFormSet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML
from crispy_forms.bootstrap import *
from .crispy_layout import PrependedField

class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ('assignName','amountQuizShort','amountQuizOne','amountQuizMulti')

    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        self.fields['assignName'].label = False
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            #PrependedText('Selection_1', 'Check', placeholder="Selection1", active=True)
            PrependedText('assignName', 'AssignName', placeholder="Assignment1", css_class='question', active=True),
            #PrependedAppendedText('Selection_1', '$', '.00', active=True)
            Div('amountQuizShort','amountQuizOne','amountQuizMulti', css_class='form-inline')
        )

'''
class Quiz_oneForm(forms.ModelForm):

    class Meta:
        model = quiz_one
        fields = ('Question', 'Answer','Wrong_1','Wrong_2','Wrong_3',)
        widgets ={
        'Question': Textarea(attrs={'cols': 80, 'rows': 5}),
        'Answer': Textarea(attrs={'cols': 80, 'rows': 1}),
        'Wrong_1': Textarea(attrs={'cols': 80, 'rows': 1}),
        'Wrong_2': Textarea(attrs={'cols': 80, 'rows': 1}),
        'Wrong_3': Textarea(attrs={'cols': 80, 'rows': 1}),
        }
'''
class Quiz_shortForm(forms.ModelForm):

    class Meta:
        model = quiz_short
        #fields = ('Question', 'Answer',)
        exclude = ('AssignNum',)
        widgets ={
        'Question': TextInput(attrs={'placeholder':'Short Answer Quiz Question','class':'form-control question'}),
        'Answer': TextInput(attrs={'placeholder':'Short Answer','class': 'form-control question'}),
        }


    '''
    def __init__(self, *arg, **kwarg):
        super(Quiz_shortForm, self).__init__(*arg, **kwarg)
        self.empty_permitted = False
    '''
class Quiz_oneForm(forms.ModelForm):
    CHECK_LIST=((1,'check11'),(2,'check22'),(3,'check33'),(4,'check44'))
    Check = forms.TypedChoiceField(choices=CHECK_LIST, widget=forms.RadioSelect, coerce=int)

    class Meta:
        model = quiz_one
        exclude = ('AssignNum',)
#        fields = ('Question','Check_1','Check_2','Check_3','Check_4','Selection_1','Selection_2','Selection_3','Selection_4',)
        #fields = ('Question','Check','Selection_1','Selection_2','Selection_3','Selection_4',)

        widgets ={
        'Question': TextInput(attrs={'placeholder':'Question','class':'form-control question'}),
        'Selection_1': TextInput(attrs={'class': 'form-control'}),
        'Selection_2': TextInput(attrs={'class': 'form-control'}),
        'Selection_3': TextInput(attrs={'class': 'form-control'}),
        'Selection_4': TextInput(attrs={'class': 'form-control'}),
        }



    def __init__(self, *args, **kwargs):
        super(Quiz_oneForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            #PrependedText('Selection_1', 'Check', placeholder="Selection1", active=True)
            Field('Question', ),
            #PrependedAppendedText('Selection_1', '$', '.00', active=True)
        )
    '''
    def __init__(self, *arg, **kwarg):
        super(Quiz_oneForm, self).__init__(*arg, **kwarg)
        self.empty_permitted = False
    '''

class Quiz_multiForm(forms.ModelForm):

    class Meta:
        model = quiz_multi
        exclude = ('AssignNum',)
        #fields = ('Check_1',)
        '''
        fields = ('Question','Selection_1','Selection_2','Selection_3','Selection_4')
        '''
        widgets ={
        'Question': TextInput(attrs={'placeholder':'Question','class':'form-control question'}),
        'Selection_1': TextInput(attrs={'class': 'form-control'}),
        'Selection_2': TextInput(attrs={'class': 'form-control'}),
        'Selection_3': TextInput(attrs={'class': 'form-control'}),
        'Selection_4': TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(Quiz_multiForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_show_labels = False
        '''
        self.helper.layout = Layout(
            Field('Question'),
            #PrependedText('Selection_1', 'Check', placeholder="Selection1", active=True)
            Div(
            PrependedField('Selection_1', 'Check_1', active=True),css_class="input-group input-group-lg"),
            PrependedField('Selection_2', 'Check_2', active=True),
            PrependedField('Selection_3', 'Check_3', active=True),
            PrependedField('Selection_4', 'Check_4', active=True)
            #PrependedAppendedText('Selection_1', '$', '.00', active=True)
            )
        '''

    '''
    def __init__(self, *arg, **kwarg):
        super(Quiz_multiForm, self).__init__(*arg, **kwarg)
        self.empty_permitted = False
    '''

class BaseQuiz_shortFormSet(BaseFormSet):
    def clean(self):

        if any(self.errors):
            return

        questions = []
        answers = []

        for form in self.forms:
            if form.cleaned_data:
                question = form.cleaned_data['Question']
                answer = form.cleaned_data['Answer']

            questions.append(question)
            answers.append()


class BaseQuiz_oneFormSet(BaseFormSet):
    def clean(self):

        if any(self.errors):
            return

        questions = []
        answers = []

        for form in self.forms:
            if form.cleaned_data:
                question = form.cleaned_data['Question']
                answer = form.cleaned_data['Answer']

            questions.append(question)
            answers.append()

class BaseQuiz_multiFormSet(BaseFormSet):
    def clean(self):

        if any(self.errors):
            return

        questions = []
        answers = []

        for form in self.forms:
            if form.cleaned_data:
                question = form.cleaned_data['Question']
                answer = form.cleaned_data['Answer']

            questions.append(question)
            answers.append()
