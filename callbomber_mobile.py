import requests
from time import sleep
i = 0
name = list()
surname = list()
name = ['Guillaume','Alexandre','Clement','Jean','Ibrahim','Kevin','Benoît','Geoffrey','Nicolas','Tom','Jules','William','Curtis']
surname = ['Leclair', 'LeRoy','Pirouet','Moreau','Fournier','Goulet','Cobain','Gaulin','Bellefeuille','Dupuy','Larocque','St-Jacques']
number = open('phonenumber.txt','r')
phonenumber = number.read()
while i < len(name) & len(surname):
	r = requests.get("https://www.carglass.fr/webservice/contact?name="+name[i]+"&surname="+surname[i]+"&e164="+phonenumber+"&delay=0&reason=NBOL&csrf_token=true")
	print("Calling"+phonenumber+"...")
	i+=1
	sleep(120)