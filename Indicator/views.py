from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Indicator

# Create your views here.


def index(request):
    indicators_list = Indicator.objects.all()
    #из всей табилицы в БД мы считаем за сколько месяцов 
    # окупиться проект со старта
    PB = calculate(indicators_list)
    return render(request, 
                'indicators.html', 
                {'indicators_list': indicators_list,
                'payback': PB} )
    
def add_indicators(request):
    month = float(request.POST['month'])
    year = request.POST['year']
    income = float(request.POST['income'])
    i = Indicator(Month = month, 
                    Year = year, 
                    Income = income)
    i.save()
    return HttpResponseRedirect(reverse('indicators:index') )

def calculate(data):
    # примем что сума инвеситций будут только в этом 
    # участке кода.
    investmanets = 13000
    PB = 0
    summm = 0
    for item in data:
        if summm <= investmanets:
            summm += item.Income
            PB += 1
    return 0 if summm < investmanets else PB
