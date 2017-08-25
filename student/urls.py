from django.conf.urls import url
from . import views
from . import randomviews

urlpatterns = [
    #url(r'^student_quiz/', views.student_quiz, name='student_quiz'),
    url(r'^student_subject', views.student_subject, name='student_subject'),
    url(r'^$', views.student_subject, name='student_subject'),
    url(r'^student_quiz/(?P<Subject_Order>[\w-]+)/$', views.student_quiz, name='student_quiz'),
    url(r'^student_take_quiz/(?P<Quiz_Order>[\w-]+)/$', views.student_take_quiz, name='student_take_quiz'),
#    url(r'^student_thank_you', views.student_thank_you, name='student_thank_you'),
    url(r'^student_take_quiz_random/(?P<Quiz_Order>[\w-]+)/$', randomviews.student_take_quiz, name='student_take_quiz_random'),
]
