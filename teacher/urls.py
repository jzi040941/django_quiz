from django.conf.urls import url
from . import views
from . import check_views

urlpatterns = [
    #url(r'^teacher_quiz/', views.teacher_quiz, name='teacher_quiz'),
    url(r'^teacher_subject/', views.teacher_subject, name='teacher_subject'),
    url(r'^$', views.teacher_subject, name='teacher_subject'),
    url(r'^teacher_quiz/(?P<subject_Num>[\w-]+)/$', views.teacher_quiz, name='teacher_quiz'),
    url(r'^teacher_quiz/(?P<subject_Num>[\w-]+)/new$', views.quiz_new, name='quiz_new'),
    url(r'^teacher_quiz/(?P<assign_Num>[\w-]+)/modify$', views.quiz_modify, name='quiz_modify'),
    url(r'^quiz_submit_check/(?P<assign_Num>[\w-]+)/$', check_views.quiz_submit_check, name='quiz_submit_check'),
#    url(r'^teacher_thank_you', views.teacher_thank_you, name='teacher_thank_you')
]
