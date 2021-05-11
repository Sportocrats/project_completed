from django.shortcuts import render, redirect

# Create your views here.
from .models import Player_Male,Player_female,admin_sports, screening_cricket_male, screening_football_male, screening_basketball_male, screening_chess_male, screening_table_tennis_male
from .models import screening_badminton_male, screening_athletics_male

from .models import cricket_male, football_male, basketball_male, chess_male, table_tennis_male, badminton_male, athletics_male
from .models import cricket_female, football_female, basketball_female, chess_female, table_tennis_female, badminton_female, athletics_female

from .models import selection_cricket_male, selection_football_male, selection_basketball_male, selection_chess_male, selection_table_tennis_male, selection_badminton_male, selection_athletics_male
from .models import selection_chess_female, selection_table_tennis_female, selection_badminton_female

def index(request):
    return render(request, 'main1.html')

def main1(request):
    return render(request, 'main1.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def announce(request):
    return render(request, 'announce.html')

def contactus(request):
    return render(request, 'contactus.html')

def screening(request):
    data = screening_cricket_male.objects.all()
    data1 = screening_football_male.objects.all()
    data2 = screening_basketball_male.objects.all()
    data3 = screening_chess_male.objects.all()
    data4 = screening_table_tennis_male.objects.all()
    data5 = screening_badminton_male.objects.all()
    data6 = screening_athletics_male.objects.all()
    return render(request, 'screening.html', {"dat" : data, "dat1" : data1, "dat2" : data2, "dat3" : data3, "dat4" : data4, "dat5" : data5, "dat6" : data6})

def trial_male(request):
    data = cricket_male.objects.all()
    data1 = football_male.objects.all()
    data2 = basketball_male.objects.all()
    data3 = chess_male.objects.all()
    data4 = table_tennis_male.objects.all()
    data5 = badminton_male.objects.all()
    data6 = athletics_male.objects.all()
    return render(request, 'trial_male.html', {"dat" : data, "dat1" : data1, "dat2" : data2, "dat3" : data3, "dat4" : data4, "dat5" : data5, "dat6" : data6})

def trial_female(request):
    data = cricket_female.objects.all()
    data1 = football_female.objects.all()
    data2 = basketball_female.objects.all()
    data3 = chess_female.objects.all()
    data4 = table_tennis_female.objects.all()
    data5 = badminton_female.objects.all()
    data6 = athletics_female.objects.all()
    return render(request, "trial_female.html", {"dat" : data, "dat1" : data1, "dat2" : data2, "dat3" : data3, "dat4" : data4, "dat5" : data5, "dat6" : data6})

def final_male(request):
    data = selection_cricket_male.objects.all()
    data1 = selection_football_male.objects.all()
    data2 = selection_basketball_male.objects.all()
    data3 = selection_chess_male.objects.all()
    data4 = selection_table_tennis_male.objects.all()
    data5 = selection_badminton_male.objects.all()
    data6 = selection_athletics_male.objects.all()
    return render(request, 'final_male.html', {"dat" : data, "dat1" : data1, "dat2" : data2, "dat3" : data3, "dat4" : data4, "dat5" : data5, "dat6" : data6})

def final_female(request):
    data3 = selection_chess_female.objects.all()
    data4 = selection_table_tennis_female.objects.all()
    data5 = selection_badminton_female.objects.all()
    return render(request, 'final_female.html', {"dat3" : data3, "dat4" : data4, "dat5" : data5})

def register(request):
    if request.method=='POST':
        first_name=request.POST['name1']
        last_name=request.POST['name2']
        email = request.POST['email']
        password = request.POST['password']
        sports = request.POST['sports']
        post=request.POST['sports']

        ins=admin_sports(first_name=first_name,last_name=last_name,email=email,password=password,sports=sports,post=post)
        ins.save()
        print("user created")
        return redirect('/')
    else:
        return render(request, 'register.html')


def male(request):
    if request.method=='POST':
        first_name=request.POST['name1']
        last_name=request.POST['name2']
        sid = request.POST['sid']
        email = request.POST['email']
        password = request.POST['password']
        sports = request.POST['sports']

        ins=Player_Male(first_name=first_name,last_name=last_name,sid=sid,email=email,password=password,sports=sports)
        ins.save()
        print("user created")
        return redirect('/')








    else:
        return render(request, 'male.html')



def female(request):
    if request.method=='POST':
        first_name=request.POST['name1']
        last_name=request.POST['name2']
        sid = request.POST['sid']
        email = request.POST['email']
        password = request.POST['password']
        sports = request.POST['sports']

        ins=Player_female(first_name=first_name,last_name=last_name,sid=sid,email=email,password=password,sports=sports)
        ins.save()
        print("user created")
        return redirect('/')

    else:
        return render(request, 'female.html')