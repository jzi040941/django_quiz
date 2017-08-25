from django.shortcuts import redirect, render

def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.groups.filter(name="teacher").exists():
        # user is an admin
        return redirect("/teacher")
    else:
        return redirect("/student")

def back_home(request):
    if request.user.groups.filter(name="teacher").exists():
        # user is an admin
        return redirect("/teacher")
    else:
        return redirect("/student")    

def logoutuser(request):
    #logout(request)
    return redirect("http://kivproject17.polito.uz:8000/")

def thank_you(request):
    return render(request, 'thank_you.html')
