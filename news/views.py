from django.shortcuts import render
import time
from django.http import HttpResponse
import requests
from datetime import timedelta
import datetime, json

def index(request):
    import requests
    url = ('https://newsapi.org/v2/everything?'
           'q=(bangalore+OR+bengaluru)+AND+(BBMP)&'
           'from='
           + str(datetime.datetime.now() - timedelta(10))[:10] +
           '&'
           'language=en&'
           'sortBy=publishedAt&'
           'apiKey=a826d75e69d840bd8d513499e63a3aaf')
    print(url)
    start = time.time()
    response = requests.get(url)
    end = time.time()
    print(end - start)
    result = dict(response.json())
    my_date = datetime.datetime.strptime(result['articles'][5]['publishedAt'][:10], "%Y-%m-%d")
    # print(my_date.strftime("%d %b, %Y"))
    return render(request, 'news/index.html', {'response': result})