from machine import Pin
from time import sleep
import dht
sensor = dht.DHT11(Pin(23))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        umid = sensor.humidity()
        print("Temperatura ", temp, "  Umidade ", umid)
        sleep(5)
    except OSError as error :
        print(error)
        print("File descriptor is not associated with any terminal device")