from django.shortcuts import render
import requests
import json
from django.contrib import messages
from django.http import HttpResponseRedirect
import random

# Create your views here.

def login(request):
    return render(request, 'login/login.html')

def login_submit(request):
    if request.method == 'POST':
        email = request.POST['Email']
        passwd = request.POST['Password']
        url = 'https://5pqr8ssuxb.execute-api.us-east-1.amazonaws.com/v1/login'
        headers = {'content-type':'application/json'}
        data = {"email": email, "password": passwd}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        #print(r.status_code)
        if r.status_code == 200:
            #api_request = json.loads(r.content)
            #print(api_request)
            return render(request,'random_password_gen.html')
        elif r.status_code == 203:
            
            messages.error(request,'Please verify your email first ')
            return HttpResponseRedirect('/')
        else:
            messages.error(request,'Invalid Credentials')
            return HttpResponseRedirect('/')
    else:
        messages.error(request,'Invalid Credentials')
        return HttpResponseRedirect('/')



def User_RegiterSubmit(request):
    if request.method =='POST':
        name = request.POST['Name']
        email = request.POST['Email']
        password = request.POST['Password']
        url = ' https://5pqr8ssuxb.execute-api.us-east-1.amazonaws.com/v1/provision'
        headers = {'content-type':'application/json'}
        data = {
            'name':name,
            'email':email,
            'password':password,
            }
        r = requests.post(url, data = json.dumps(data), headers=headers)
        if r.status_code ==200:
          messages.success(request, 'User Registered Successfully. Please verify your email')
          return HttpResponseRedirect('/')
        else:
          messages.warning(request,'User Alredy Exits For This Student ID')
          return HttpResponseRedirect('/')
    else:
        messages.warning(request,'User Alredy Exits For This Student ID')
        return HttpResponseRedirect('/')


def listpass(request):
    url = 'https://5pqr8ssuxb.execute-api.us-east-1.amazonaws.com/v1/pass-gen/?email=sujeetsingh0094@gmail.com'
    headers = {'content-type':'application/json'}
    r = requests.get(url,headers=headers)
    api_request = json.loads(r.content)
    if r.status_code == 200:
        return render(request, 'listdata.html', {"api_request":api_request})
    else:
        return render(request, 'listdata.html')

def deletepass(request, id):
    url = 'https://5pqr8ssuxb.execute-api.us-east-1.amazonaws.com/v1/pass-gen/?id='+id
    headers = {'content-type':'application/json'}
    r = requests.delete(url,headers=headers)
    if r.status_code == 200:
        messages.success(request, 'Deleted successfully')
        return HttpResponseRedirect('/listpass/')
    else:
        return HttpResponseRedirect('/listpass/')

def listpass_submit(request):
    if request.method == 'POST':
        username="sujeetsingh0094@gmail.com"
        app = request.POST['app']
        passwd = request.POST['passwd']
        url = 'https://5pqr8ssuxb.execute-api.us-east-1.amazonaws.com/v1/pass-gen'
        headers = {'content-type':'application/json'}

        add_pass = {"app": app, "passwd": passwd, "username": username}
        r = requests.post(url, data=json.dumps(add_pass), headers=headers)
        print(r)
        if r.status_code == 200:
            messages.success(request,'Added successfully')
            api_request = json.loads(r.content)
            print(api_request)
            print(r.status_code)
            return HttpResponseRedirect('/listpass/')
        else:
            messages.error(request,'Invalid Credentials')
            #return HttpResponseRedirect('/')
            return HttpResponseRedirect('/listpass/')
    else:
        messages.error(request,'method not found')
        return HttpResponseRedirect('/')


def backlistdata(request):
    return render(request, 'random_password_gen.html')

def addpass(request):
    return render(request, 'addpass.html')




# def password(request):
#     characters = list('abcdefghijklmnopqrstuvwxyz')

#     if request.GET.get('uppercase'):
#         characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

#     if request.GET.get('numbers'):
#         characters.extend(list('0123456789'))

#     if request.GET.get('special'):
#         characters.extend(list('!@#$%^&*()?><:;'))

#     length = int(request.GET.get("length"))

#     thepassword = ''
#     for x in range(length):
#         thepassword += random.choice(characters)

#     return render(request, 'password.html', {"password":thepassword})

