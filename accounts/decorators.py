from django.http import HttpResponse
from django.shortcuts import redirect

def anauthanticated_user(view_func):
    # view_func its aparameter to decorator and it will revranc or back to any function in the view
    def warpper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:  
           return view_func(request, *args, **kwargs)
  
    return warpper_func


def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                
            if group in allowed_roles:
             return view_func(request, *args, **kwargs)
            else:
             return HttpResponse('you are not allow to show this page')
         
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):        
        group = None
        if request.user.groups.exists():
           group = request.user.groups.all()[0].name
                
        if group == 'customer':
            return redirect('user-page')
        
        if group == 'admin':           
            return view_func(request, *args, **kwargs)
       
    return wrapper_function