#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import random

# Set up GPIO using BCM numbering and disable warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set pin number for each LED
led0 = 4
led1 = 17
led2 = 27
led3 = 22
led4 = 18
led5 = 23
led6 = 24
led7 = 25

# Put all LED pins into a list
leds = [led0, led1, led2, led3, led4, led5, led6, led7]

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

# Flashes odd numbered LEDS, then even numbered LEDs
def Danger(delay):
	while(True):
		GPIO.output(leds, GPIO.LOW)
		GPIO.output(leds[::2], GPIO.HIGH)
		time.sleep(delay)
		GPIO.output(leds, GPIO.LOW)
		GPIO.output(leds[1::2], GPIO.HIGH)
		time.sleep(delay)

# Flashes LEDs like a line of marching ants
def Ants(delay):
	while(True):
		GPIO.output(leds, GPIO.LOW)
		GPIO.output(leds[::3], GPIO.HIGH)
		time.sleep(delay)
		GPIO.output(leds, GPIO.LOW)
		GPIO.output(leds[1::3], GPIO.HIGH)
		time.sleep(delay)
		GPIO.output(leds, GPIO.LOW)
		GPIO.output(leds[2::3], GPIO.HIGH)
		time.sleep(delay)

try:
	Ants(0.5)
except KeyboardInterrupt: # Runs cleanup on exiting by keyboard interrupt
    GPIO.cleanup()
