import requests
import emoji
degree_sign = u'\N{DEGREE SIGN}'

print("CITY WEATHER PREDICTOR")
print("-----------------------")
apikey = input("Enter your API Key :")

city = input("Enter your city : ")

url='http://openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'.format(city,apikey)

res = requests.get(url)
data = res.json()

temp = data['main']['temp']
weather=data['weather'][0]['main']
print('\n')
print('City : {}'.format(city))
print('Temperature')
print('------------')
print('Temperature in Celcius: {} {} C'.format(temp,degree_sign))
fahren=(temp*(9/5))+32
print('Temperature in Fahrenheit: {} {} F'.format(fahren,degree_sign))
print('\n')
print("Today's weather forecast:")
print('--------------------------')
if(weather=="Thunderstorm"):
    print("Thunderstorm")
    print(emoji.emojize(":cloud_lightning:"))
elif(weather=="Drizzle"):
    print("Drizzle")
    print(emoji.emojize(":umbrella:"))
elif(weather=="Snow"):
    print("Snow")
    print(emoji.emojize(":snowflake:"))
elif(weather=="Clear"):
    print("Clear")
    print(emoji.emojize(":sun_with_face:"))
elif(weather=="Clouds"):
    print("Clouds")
    print(emoji.emojize(":cloud:"))
elif (weather=="Mist" or weather=="Smoke" or weather=="Haze" or weather=="Fog"):
    if(weather=="Mist"):
        print("Mist")
    elif(weather=="Smoke"):
        print("Smoke")
    elif(weather=="Haze"):
        print("Haze")
    else:
        print("Fog")
    print(emoji.emojize(":foggy:"))
else:
    if(weather=="Dust"):
        print("Dust")
    elif(weather=="Sand"):
        print("Sand")
    elif(weather=="Squall"):
        print("Squall")
    elif(weather=="Tornado"):
        print("Tornado")
    else:
        print("Ash")
    print(emoji.emojize(":cloud_tornado:"))

