from django.shortcuts import render

def home(request):
    import requests
    import json
    #grab price data
    price_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,LTC,EOS,XLM,ADA,USDT&tsyms=USD")
    price=json.loads(price_request.content)


    #grab news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {"api":api,"price":price})
  
def prices(request):
   
    if request.method=="POST":
        import requests
        import json
        quote=request.POST['quote']
        quote=quote.upper()
        crypto_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto=json.loads(crypto_request.content)
        return render(request, 'prices.html' ,{'quote':quote,'crypto':crypto})

    else:
        notfound="enter curr above in form..."
        return render(request,'prices.html',{'notfound':notfound})