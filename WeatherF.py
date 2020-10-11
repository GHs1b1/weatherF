# Application that interact with webservice to obtain data.

import requests

location: str = input("Enter the city name: ")

try:
    print(location)
except:
    print('invalid city, please re-enter')


def main():
    # website: "https://api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API
    # key}"
    url: str = "http://api.openweathermap.org/data/2.5/weather?q=Stroudsburg,pa,us&units=imperial&APPID=e4e38cc148c3f9ba2ed55980157cd226"
    res = requests.get(url)

    data = res.json()

    print(res.text)

    print(data)

    if data['cod'] == '404':
        print("Invalid data:{}, please check data and re-enter information")
    else:
        print(res.json())

    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    humdt = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print("-----------------------------------------")
    print("-------------------------------------------")
    print('temperature: ', temperature)
    print('wind_speed: {}', format(wind_speed))
    print('humidity: ', humdt, '%')
    print('weather_description: {}', format(weather_description))


main()
