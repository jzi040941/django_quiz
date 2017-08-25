import django_tables2 as tables
from student.models import SubmitAssign

class SubmitAssignTable(tables.Table):
    class Meta:
        model = SubmitAssign
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
