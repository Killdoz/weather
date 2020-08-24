import time
import pyowm

print("choose your city")
city = str(input())

owm = pyowm.OWM("d446acc2744bedf951927f5d95938302")

mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather

temp = w.temperature('celsius')['temp']

print("В городе " + city + " сейчас " + str(temp) + " градусов!")
time.sleep(5)