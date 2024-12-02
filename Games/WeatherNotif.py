import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()

def getdata(url):
    r = requests.get(url)
    return r.text

htmldata = getdata("https://weather.com/weather/today/l/81875498401fd1c269fb07dce364db25ab4ee18a60c2ce3fedf0cee8f172016c")

soup = BeautifulSoup(htmldata, 'html.parser')

current_temp  = soup.find_all("span", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions-tempValue--MHmYY")

chances_rain = soup.find_all("div", class_="_-_-components-src-organism-CurrentConditions-precipValue--2aJSf")

temp = (str(current_temp))

temp_rain = str(chances_rain)

result = "current_temp" + temp[128:-9] + " in kathmandu nepal" + "\n" + temp_rain[131:14]
n.show_toast("live weather update",result, duration= 10)