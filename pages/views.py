from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as llogin
from django.shortcuts import redirect
from .models import Rozliczenia, Documents
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from users.models import CustomUser
from django.core.files.storage import default_storage


# Create your views here.
def home(request):
    if not request.user.is_authenticated:
       return redirect('/pickpage')
    elif request.user.verificated == True:
        return render(request, 'index.html')
    else:  
        return redirect('addinfo_view')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, "register.html")

def register(request):
    email1 = request.POST['email1']
    password = request.POST.get('pass1')
    user = CustomUser.objects.create_user(email1, password)
    user.save()
    return redirect('/')

def login(request):
    username = request.POST.get('email1')
    password = request.POST.get('pass1')
    user = authenticate(username=username, password=password)
    if user is not None:
        llogin(request, user)
        return redirect('/')
    else:
        return redirect('login_view')

def pickpage(request):
    return render(request, "pickpage.html")

def documents_view(request):
    try:
        documents = Documents.objects.filter(dlakogo=request.user)
        context = {

        "documentlist":documents

        }
        return render(request, 'documents.html', context)
    except:
        return render(request, 'documents.html')

def senddocuments(request):
    typdokumentu = request.POST.get('documenttype')
    filet = request.FILES['plik']
    usr = Documents.objects.create(dokument=filet, typ_dokumentu=typdokumentu, dlakogo=request.user)
    usr.save()
    return redirect('home')

def changeinfo_view(request):
    return render(request, 'changeinfo.html')

def changeinfo(request):
    payform = request.POST.get('payform')
    banknumber = request.POST.get('banknumber')
    CustomUser.objects.filter(id=request.user.id).update(banknumer=banknumber, Forma_Wypłaty=payform)
    return redirect('/')

def earn_view(request):
    rozliczenia = Rozliczenia.objects.filter(dlakogo=request.user)
    context = {

        "rozliczenialist":rozliczenia

    }
    return render(request, 'earn.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

def addinfo_view(request):
    return render(request, "addinfo.html")

def addinfo(request):
    pesel = request.POST.get('pesel')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    idnumer = request.POST.get('idnumer')
    birth = request.POST.get('birth')
    ulica = request.POST.get('ulica')
    numerdomu = request.POST.get('numerdomu')
    kodpocztowy = request.POST.get('kodpocztowy')
    app = request.POST.get('app')
    miasto = request.POST.get('miasto')
    srodek_transportu = request.POST.get('srodek_transportu')
    ukraina = request.POST.get('ukraina')
    polak = request.POST.get('polak')
    reu = request.POST.get('reu')
    kartapobyturodzina = request.POST.get('kartapobyturodzina')
    bialorus = request.POST.get('bialorus')
    obywateleu = request.POST.get('obywateleu')
    CustomUser.objects.filter(id=request.user.id).update(pesel=pesel, imie=fname, nazwisko=lname, numer_dokumentu=idnumer,data_urodzenia=birth,ulica=ulica,numer_domu=numerdomu,kod_pocztowy=kodpocztowy,aplikacja=app, miasto=miasto, srodek_transportu=srodek_transportu, Jestem_Z_Ukrainy=ukraina, Mam_Kartę_Polaka=polak,  Rezydent_EU=reu, Karta_Pobytu_Połączenia_Z_Rodzina=kartapobyturodzina, Wiza_21_lub_23_BiznesHub=bialorus, Obywatel_EU=obywateleu, verificated=True)
    return redirect('/home/')