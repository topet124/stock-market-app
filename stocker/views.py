from django.shortcuts import render, redirect
from .models import stock
from django.contrib import messages
from .forms import stockform 
# Create your views here.
def home(request):
    import requests
    import json
    
    if request.method== 'POST':
        ticker= request.POST['ticker']
        api_get = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_8e7eab69e22b48fe847bec022e2e6508")
        
        try:
            api=json.loads(api_get.content)
        except Exception as e:
            api= "errrrrrorrr check work"
        return render(request, 'home.html',{'api':api})
    else:
            return render(request, 'home.html',{'ticker':"enter tinker symbol"})


def about(request):
    return render(request, 'about.html',{})

def stockpage(request):
    import requests
    import json
    output=[]
    if request.method== 'POST':
        form = stockform(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("stock has been added"))
            return redirect('stockpage')
    else:
        ticker =stock.objects.all()
        for ticker_item in ticker:
            api_get = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_8e7eab69e22b48fe847bec022e2e6508")
            
            try:
                api=json.loads(api_get.content)
                output.append(api)
            except Exception as e:
                api= "errrrrrorrr check work"
        return render(request, 'stockpage.html',{'ticker':ticker, 'output':output})

def delete(request, stock_id):
    item = stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request,("it has been deleted"))
    return redirect('stockpage')
