from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout


# log in
def signin(request):
    # get username, pwd parameter from  HTTP POST req
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    # verify from Django auth
    user = authenticate(username=userName, password=passWord)

    #
    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                # save usertype into session
                request.session['usertype'] = 'user'

                return JsonResponse({'ret': 0})
            else:
                return JsonResponse({'ret': 1, 'msg': 'please login'})
        else:
            return JsonResponse({'ret': 0, 'msg': 'user foorbidden'})

    #
    else:
        return JsonResponse({'ret': 1, 'msg': 'username of password incorrect'})


# logout
def signout(request):

    logout(request)
    return JsonResponse({'ret': 0})