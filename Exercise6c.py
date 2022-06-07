#import thingspeak library
#pip3 install thingspeak

import thingspeak
from time import sleep
import board
import adafruit_dht
dhtDevice = adafruit_dht.DHT22(board.D17, use_pulseio=False)


import time



channel_id=1616752
write_key ='YE95JMMNETI7ZHNG'
read_key='A4JZTVF8P7JQEWVZ'

def readDHT22():
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
    except:
        temperature_c =0
        humidity=0
    return (humidity, temperature_c)



while True:
    
    
    #Temp and Humidity Data
    humidity, temperature = readDHT22()
    
    if temperature==0 and humidity==0:
        pass
    else:
        channel = thingspeak.Channel(channel_id,write_key)
        response=channel.update({'field1':temperature,'field2':humidity})
        print(temperature,humidity)
    sleep(5)
    