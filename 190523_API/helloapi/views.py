from django.shortcuts import render, redirect
import requests, json

# Create your views here.

def navermap(request):
    return render(request, 'helloapi/navermap.html')

def kakaopay(request):
    return render(request, 'helloapi/kakaopay.html')
    
def ok(request):
    return render(request, 'helloapi/ok.html')
    
def ready(request):
    url = 'https://kapi.kakao.com/v1/payment/ready'
    headers = {'Authorization': 'KakaoAK f0505475899a63e2b557b23dbd496ff9'}
    data = {
        'cid': 'TC0ONETIME',
        'partner_order_id': '123',
        'partner_user_id': '123',
        'item_name': 'Chocolate',
        'quantity': 1,
        'total_amount': 2200,
        'vat_amount': 200,
        'tax_free_amount': 0,
        'approval_url': 'https://noori-190523-cydshin.c9users.io/success',
        'fail_url': 'https://noori-190523-cydshin.c9users.io/fail',
        'cancel_url': 'https://noori-190523-cydshin.c9users.io/cancel',
    } 
    response = requests.post(url=url, data=data, headers=headers)
    result = response.json()
    request.session['tid'] = result['tid']
    return redirect(result['next_redirect_pc_url'])
    
def success(request):
    url = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {'Authorization': 'KakaoAK f0505475899a63e2b557b23dbd496ff9'}
    data = {
        'cid': 'TC0ONETIME',
        'tid': request.session['tid'],
        'partner_order_id': '123',
        'partner_user_id': '123',
        'pg_token': request.GET['pg_token']
    }
    response = requests.post(url=url, data=data, headers=headers)
    result = response.json()
    item_name = result['item_name']
    item_price = result['amount']['total']
    return render(request, 'helloapi/ok.html', {'item_name': item_name, 'item_price': item_price})
    