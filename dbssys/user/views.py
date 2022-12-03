from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from common.models import Transaction
import json
#to integrate with .html frontend, define html template (it's should be a string) first
html_template = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>id</th>
        <th>name</th>
        <th>phonenumber</th>
        <th>address</th>
        <th>email</th>
        </tr>

        {% for customer in customers %}
            <tr>

            {% for name, value in customer.items %}            
                <td>{{ value }}</td>            
            {% endfor %}
            
            </tr>
        {% endfor %}
                
        </table>
    </body>
</html>
'''
from django.template import engines
django_engine = engines['django']
template = django_engine.from_string(html_template)

# return true data from database

def dispatcher(request):
    if request.method =="GET":
        request.params = request.GET
    else:
        request.params = json.loads(request.body)
    action = request.params['action']
    if action == 'list_transaction':
        return listtranaction(request)
    else:
        return JsonResponse({'ret': 1, 'msg': 'http request not supported'})

def listtransactions(request):
    qs = Transaction.objects.values()
    retStr = ''
    for transactions in qs:
        for name, value in transactions.items():
            retStr += f'{name}:{value} |'
        retStr += '<br>' #new line
    return HttpResponse(retStr)



'''
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': 'not signed in',
            'redirect': '/mgr/sign.html'},
            status=302)

    if request.session['usertype'] != 'mgr':
        return JsonResponse({
            'ret': 302,
            'msg': 'user not mgr',
            'redirect': '/mgr/sign.html'} ,
            status=302)
'''

