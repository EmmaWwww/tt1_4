from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout


# login
def signin(request):
    # get username,pwd from  HTTP POST request
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    # Django auth verification
    user = authenticate(username=userName, password=passWord)

    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                # store usetype into session
                request.session['usertype'] = 'user'

                return JsonResponse({'ret': 0})
            else:
                return JsonResponse({'ret': 1, 'msg': 'pls login'})
        else:
            return JsonResponse({'ret': 0, 'msg': 'user unauthorised'})

    else:
        return JsonResponse({'ret': 1, 'msg': 'username or password incorrect'})


# log out
def signout(request):
    #
    logout(request)
    return JsonResponse({'ret': 0})