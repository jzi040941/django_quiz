from django.contrib.auth.models import Group

class FilterTeacherMiddleware(object, Group):
    #Check if client is student
    def process_request(self, Group):
        users_in_group = Group.objects.get(name="teacher").user_set.all()
        if user not in users_in_group:
            raise Http403
            #If not Student don't let access

        # If Student we don't do anything
        return None
