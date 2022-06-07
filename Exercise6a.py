#Exercise6a.py
#Library
from time import sleep
import board
import adafruit_dht

#Setup
dhtDevice=adafruit_dht.DHT22(board.D17,use_pulseio=False)

#Function
def readDHT22():
    try:
        #sensor reads correctly
        temperature_c = dhtDevice.temperature
        humidity=dhtDevice.humidity
    except:
        #sensor mulfunction
        temperature_c=0
        humidity=0
    return (humidity,temperature_c)

#Algorithm
while True:
    humidity,temperature=readDHT22()
    print(humidity,temperature)
    sleep(5)