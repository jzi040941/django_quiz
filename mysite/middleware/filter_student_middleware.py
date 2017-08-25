from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.conf import settings
from re import compile


EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/student/'):
            if not request.user.is_authenticated():
                return HttpResponseRedirect("/")
            if request.user.groups.filter(name="teacher").exists():
                return HttpResponseRedirect("/teacher/")

        if request.path.startswith('/teacher/'):
            if not request.user.is_authenticated():
                return HttpResponseRedirect("/")
            if request.user.groups.filter(name="student").exists():
                return HttpResponseRedirect("/student/")

        return self.get_response(request)
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
    you can copy from your urls.py).

    Requires authentication middleware and template context processors to be
    loaded. You'll get an error if they aren't.
    """
    def process_request(self, request):
        assert hasattr(request, 'user'), "The Login Required middleware\
 requires authentication middleware to be installed. Edit your\
 MIDDLEWARE_CLASSES setting to insert\
 'django.contrib.auth.middlware.AuthenticationMiddleware'. If that doesn't\
 work, ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes\
 'django.core.context_processors.auth'."
        if not request.user.is_authenticated():
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                return HttpResponseRedirect(settings.LOGIN_URL)

class FilterStudentMiddleware(object):


    def __init__(self, get_response):
        self.get_response = get_response
        print("hello1")

    def __call__(self, request):
        print("hello2")
        self.process_request(request)
        #if not request.user.is_authenticated():
        #    return HttpResponseRedirect("/")
        '''
        if request.path.startswith('/student/'):
            if not request.user.is_authenticated():
                return HttpResponseRedirect("/")
        return self.get_response(request)
        '''
        '''
        assert hasattr(request, 'user'), "The Login Required middleware\
 requires authentication middleware to be installed. Edit your\
 MIDDLEWARE_CLASSES setting to insert\
 'django.contrib.auth.middleware.AuthenticationMiddleware'. If that doesn't\
 work, ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes\
 'django.core.context_processors.auth'."
        '''
        '''
        if not request.user.is_authenticated():
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                return HttpResponseRedirect(settings.LOGIN_URL)
        '''

    #Check if client is student
    def process_request(self, request):
        print("hahahahaha")



'''
        users_in_group = request.user.groups.filter(name="teacher").exists()
        if users_in_group:
            raise Http403
            #If not Student don't let access

        # If Student we don't do anything
        return None
'''
