import requests
degree_sign = u'\N{DEGREE SIGN}'
from pprint import pprint
city = input("Enter your city : ")
apikey = input("Enter your API Key")
url='http://openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'.format(city,apikey)
res = requests.get(url)
data = res.json()
temp = data['main']['temp']
print('Temperature : {} {} C'.format(temp,degree_sign))
