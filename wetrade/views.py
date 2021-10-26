# from websocket import create_connection
from django.shortcuts import render
from websocket import create_connection
from urllib.parse import urlparse
import urllib.request
import urllib.parse
import urllib.error
import json
# import requests
# from django.http import HttpResponse
# from json.decoder import JSONDecodeError
# import time
# https: // api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-17?apiKey = _KA8er2SJzFwUY6tmHvHsQrvGOMEHpOv
def todo(request):
    list1 = []
    # url = "https://www.coinapi.io/pricing?apiKey=F3F302E7-CB58-46DD-B55D-C8EAF4BAAEB3"
    url = "https://api.polygon.io/v1/meta/crypto-exchanges?apiKey=_KA8er2SJzFwUY6tmHvHsQrvGOMEHpOv"
    print('Retrieving', url)
    endpoint = (urllib.request.urlopen(url).read())
    data = endpoint.decode()
    data1 = json.loads(data)
    print("type",type(data1))
    for item in data1:
        list1.append(item)
    print(list1)

    # url = "https: // api.polygon.io/v1/meta/crypto-exchanges?apiKey = _KA8er2SJzFwUY6tmHvHsQrvGOMEHpOv"
    # data = urllib.request.urlopen(url)
    # data1 = data.read().decode('ascii')
    return render(request, 'home.html', {'list1':list1})


# def coin(request):
#     list2 = []
#     url = "https://www.coinapi.io/pricing?apiKey=F3F302E7-CB58-46DD-B55D-C8EAF4BAAEB3"
#     print('Retrieving', url)
#     endpoint = (urllib.request.urlopen(url).read())
#     data3 = endpoint.decode()
#     data2 = json.loads(data3)
#     print("type", type(data2))
#     for item in data2:
#         list2.append(item)
#     print(list2)

#     return render(request, 'home.html', {'list2': list2})

