from django.shortcuts import render
from django.http import HttpResponse
from django.template import engines
django_engine = engines['django']
template = django_engine.from_string(html_template)
from common.models import Profile, Transaction,Account

# Create your views here.
def listtransactions(request):
    # 根据session判断用户是否是登录的管理员用户
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': 'not signed in',
            'redirect': '/<frontend unzipped dir>/<sign>.html'},
            status=302)

    if request.session['usertype'] != '<usertype>':
        return JsonResponse({
            'ret': 302,
            'msg': 'user not <usertype>',
            'redirect': '/<frontend unzipped dir>/<sign>.html'} ,
            status=302)

    #QuerySet object return all element from table
    qs = Transaction.objects.values() #refer to common.model.py table settings
    retStr = ''
    for transactions in qs:
        for name, value in transactions.items():
            retStr += f'{name}:{value} |'
        retStr += '<br>' #new line
    return HttpResponse(retStr)
