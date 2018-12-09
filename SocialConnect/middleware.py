
import re
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

EXEMPT_URLS=[re.compile(settings.LOGIN_URL.lstrip('/'))]
LOGIN_REDIRECT_URL=settings.LOGIN_REDIRECT_URL
if hasattr(settings,"LOGIN_EXEMPT_URLS"):
    EXEMPT_URLS+=[re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_view(self,request,view_fun,view_args,view_kwargs):
        assert hasattr(request,'user')  
        path=request.path_info.lstrip('/')
        print("path is ",path) 


        # if path == reverse('logout').lstrip('/'):
        #     logout(request)
        url_is_exempt=any(url.match(path)for url in EXEMPT_URLS)
        if  request.user.is_authenticated and url_is_exempt:
            # return redirect(settings.LOGIN_URL)
            return None

        elif not request.user.is_authenticated and url_is_exempt :
            # return redirect(settings.LOGIN_URL)
            return None
        else:
            # return redirect(settings.LOGIN_URL)
            return None

            

