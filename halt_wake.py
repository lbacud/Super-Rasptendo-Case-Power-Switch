#!/usr/bin/env python3
from gpiozero import Button, LED
import os 
from signal import pause

gpioPin = 3 #a Raspberry Pi "wakes up" from a halt state when GPIO3 (pin 5) is shorted to ground (GND)
rebootPin = 27 #GPIO27 (pin 13) for soft reboot
hold = 1
led = LED(14)
led.on()

#functions that handle button events
def halt():
  os.system("sudo shutdown -h now")
def when_pressed():
  led.blink(.2,.2)
def when_released():
  led.on()
def reboot(): 
  os.system("sudo reboot")
  
btn = Button(gpioPin, hold_time=hold)
rebootBtn = Button(rebootPin)
rebootBtn.when_pressed = reboot 
btn.when_held = halt 
btn.when_pressed = when_pressed
btn.when_released = when_released
pause()
