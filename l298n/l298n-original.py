import RPi.GPIO as gpio
import time

pin1 = 24
pin2 = 25
pin3 = 8
pin4 = 7

def init():
  gpio.setmode(gpio.BCM)
  gpio.setup(pin1, gpio.OUT)
  gpio.setup(pin2, gpio.OUT)
  gpio.setup(pin3, gpio.OUT)
  gpio.setup(pin4, gpio.OUT)

def forward(sec):
  init()
  gpio.output(pin1, True)
  gpio.output(pin2, False)
  gpio.output(pin3, True) 
  gpio.output(pin4, False)
  time.sleep(sec)
  gpio.cleanup()

def reverse(sec):
  init()
  gpio.output(pin1, False)
  gpio.output(pin2, True)
  gpio.output(pin3, False) 
  gpio.output(pin4, True)
  time.sleep(sec)
  gpio.cleanup()

print("forward")
forward(4)
print("reverse")
reverse(2)
