from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
for y in range(5):
    led.value(1)
    sleep(1)
    print('liga')
    led.value(0)
    sleep(1)