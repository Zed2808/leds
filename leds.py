#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import random

# Set up GPIO using BCM numbering and disable warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set pin number for each LED
led1 = 4
led2 = 17
led3 = 27
led4 = 22
led5 = 18
led6 = 23
led7 = 24
led8 = 25

# Put all LED pins into a list
leds = [led1, led2, led3, led4, led5, led6, led7, led8]

# Set all LED pins as outputs and set them LOW
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, GPIO.LOW)


# Strobes LEDs back and forth one-by-one
def Strobe(delay):
	while(True):
		for i in leds:
			GPIO.output(leds, GPIO.LOW)
			GPIO.output(i, GPIO.HIGH)
			time.sleep(delay)
		for i in reversed(leds):
			GPIO.output(leds, GPIO.LOW)
			GPIO.output(i, GPIO.HIGH)
			time.sleep(delay)

# Flashes a random LED every <delay> seconds
def RandomBlink(delay):
	while(True):
		GPIO.output(leds, GPIO.LOW)
		GPIO.output(random.sample(leds, 1), GPIO.HIGH)
		time.sleep(delay)

try:
    Strobe(0.05)
except KeyboardInterrupt: # Runs cleanup on exiting by keyboard interrupt
    GPIO.cleanup()
