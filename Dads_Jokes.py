import requests
import random
import pyfiglet
print(pyfiglet.figlet_format(('Dads Jokes')))
url = 'https://icanhazdadjoke.com/search'
a = input('Input your topic for the joke : ')
responce = requests.get(
	url, 
	headers={'Accept': 'application/json'},
	params={ 'term' : a}
	)
data = responce.json()
n= len(data['results'])
if(n>1):
	print(f'I got {n} jokes from your topic {a}')
	r = random.randint(0,n)
	print(data['results'][r]['joke'])
elif(n==1):
	print(f'I got {n} jokes from your topic {a}')
	print(data['results'][1]['joke'])

else:
	print(f' I got zero jokes from your topic {a}')
