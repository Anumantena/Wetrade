from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Request, Session
from django.shortcuts import render
import json
import requests


def api(request):

    #92DF2C45-4BC2-4163-A69F-9C7AD91A20A8 - new
    #F3F302E7-CB58-46DD-B55D-C8EAF4BAAEB3 - old
    # BTC AND ETH FROM FIRST API

    b_url = 'https://rest.coinapi.io/v1/exchangerate/BTC?invert=false'
    b_headers = {'X-CoinAPI-Key': '92DF2C45-4BC2-4163-A69F-9C7AD91A20A8'}
    b_response = requests.get(b_url, headers=b_headers)
    b_data = b_response.json()
    e_url = 'https://rest.coinapi.io/v1/exchangerate/ETH?invert=false'
    e_headers = {'X-CoinAPI-Key': '92DF2C45-4BC2-4163-A69F-9C7AD91A20A8'}
    e_response = requests.get(e_url, headers=e_headers)
    e_data = e_response.json()
    for item in b_data['rates']:
        if item['asset_id_quote'] == 'BUSD':
            rate_BTC = item['rate']
    for item in e_data['rates']:
        if item['asset_id_quote'] == 'BUSD':
            rate_ETH = item['rate']

    # BTC AND ETH FROM SECOND API

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '5000',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '572c340c-73a3-48e8-8c7e-28587b52a24e',
    }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        for item in data['data']:
            if item['symbol'] == 'BTC':
                rate1_BTC = item['quote']['USD']['price']
            if item['symbol'] == 'ETH':
                rate1_ETH = item['quote']['USD']['price']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("exception", e)

    # Comparision

    # if rate_BTC < rate1_BTC or rate_ETH < rate1_ETH:
    #     print('Exchange A has less value')
    # elif rate_BTC > rate1_BTC or rate_ETH > rate1_ETH:
    #     print('Exchange B has less value')

    return render(request, 'home.html', {'rateBTC': rate_BTC, 'rateETH': rate_ETH, 'rate1BTC': rate1_BTC, 'rate1ETH': rate1_ETH})
