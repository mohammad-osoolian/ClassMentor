from django.shortcuts import render
from . models import *
from django.http import HttpResponse

def intro(request):
    if request.method == 'GET':
        return render(request, 'intro.html')

def fillform(request):
    if request.method == 'GET':
        return render(request, 'form.html')
    if request.method == 'POST':
        ostad = request.POST['ostad']
        tadris = request.POST['tadris']
        nomre = request.POST['nomre']
        akhlagh = request.POST['akhlagh']
        detailes = request.POST['detailes']
        form.objects.create(ostad=ostad, tadris=tadris, nomre=nomre, akhlagh=akhlagh, detailes=detailes)
        return render(request, 'thanks.html')

def select(request):
    if request.method == 'GET':
        return render(request, 'select.html')
    
    if request.method == 'POST':
        ostad = request.POST['selectostad']
        ostadforms = form.objects.filter(ostad=ostad)
        context = makeinfo(ostadforms)
        return render(request, 'info.html', context=context)

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User = user.objects.get(username=username)
        except Exception:
            return HttpResponse(f"username {username} dosn't found")
        if User.password == password:
            return render(request, 'intro.html', context={'user':User})
        else:
            return HttpResponse('wrong username or password')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        lastname = request.POST['lastname']
        print('###')
        print(user.objects.filter(username=username))
        try:
            a = user.objects.get(username = username)
            return HttpResponse('there is an account with this username. sign in or create a new account')
        except Exception:
            user.objects.create(name=name, lastname=lastname, username=username, password=password)
            return HttpResponse('account created sucsess fully')

def learn(request):
    if request.method == 'GET':
        return render(request, 'learn.html')
    if request.method == 'POST':
        print("#############################")
        print(request.POST)

def makeinfo(ostadforms):
    tadris_marks = []
    nomre_marks = []
    akhlagh_marks = []
    detailes_texts = []
    for form in ostadforms:
        tadris_marks.append(form.tadris)
        nomre_marks.append(form.nomre)
        akhlagh_marks.append(form.akhlagh)
    context = {}
    try:
        ostadid = ostadforms[0].ostad
        if ostadid == 'SaulehEtemadi':
            context['ostad'] = 'Sauleh Etemadi'
        elif ostadid == 'MohammadZahedimoghaddam':
            context['ostad'] = 'Mohammad Zahedimoghaddam'
        elif ostadid == 'MahboobehTaghizade':
            context['ostad'] = 'Dr Mahboobeh Taghizade'
        elif ostadid == 'ElhamFattahi':
            context['ostad'] = 'Elham Fattahi'
        elif ostadid == 'MahboobehTaghizade':
            context['ostad'] = 'Mahboobeh Taghizade'
        elif ostadid == 'MarziehMaleki':
            context['ostad'] = 'Marzieh Maleki'

    except Exception:
        context['ostad'] = 'No one has filled any form about this ostad. Be the first one!'
    context['avgtadris'] = avg(tadris_marks)
    context['avgnomre'] = avg(nomre_marks)
    context['avgakhlagh'] = avg(akhlagh_marks)
    context['allforms'] = ostadforms
    return context

        

def avg(li):
    if li!=[]:
        mul = 0
        for n in li:
            mul+=n
        return round(mul/len(li), 1)
    elif li == []:
        return ''