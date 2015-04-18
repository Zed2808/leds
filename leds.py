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
	for i in leds:                      # Turns off all LEDs, then turns on next LED in the list
		GPIO.output(leds, GPIO.LOW)
		GPIO.output(i, GPIO.HIGH)
		time.sleep(delay)
	for i in reversed(leds):            # Does the same as above, but in reverse order
		GPIO.output(leds, GPIO.LOW)
		GPIO.output(i, GPIO.HIGH)
		time.sleep(delay)

# Flashes a random LED every <delay> seconds
def RandomBlink(delay):
	GPIO.output(leds, GPIO.LOW)
	GPIO.output(random.sample(leds, 1), GPIO.HIGH) # Turns on one random LED from the list
	time.sleep(delay)

# Flashes odd numbered LEDS, then even numbered LEDs
def Danger(delay):
	GPIO.output(leds, GPIO.LOW)
	GPIO.output(leds[::2], GPIO.HIGH)  # Turns on every second LED starting from index 0
	time.sleep(delay)
	GPIO.output(leds, GPIO.LOW)
	GPIO.output(leds[1::2], GPIO.HIGH) # Turns on every second LED starting from index 1
	time.sleep(delay)

# Flashes LEDs like a line of marching ants
def Ants(delay):
	GPIO.output(leds, GPIO.LOW)
	GPIO.output(leds[::3], GPIO.HIGH)  # Turns on every third LED starting from index 0
	time.sleep(delay)
	GPIO.output(leds, GPIO.LOW)
	GPIO.output(leds[1::3], GPIO.HIGH) # Turns on every third LED starting from index 1
	time.sleep(delay)
	GPIO.output(leds, GPIO.LOW)
	GPIO.output(leds[2::3], GPIO.HIGH) # Turns on every third LED starting from index 2
	time.sleep(delay)

# Turns on LEDs one-by-one, then turns them off in the same order
def Line(delay):
	for i in leds:                # Turns on each LED in the list
		GPIO.output(i, GPIO.HIGH)
		time.sleep(delay)
	for i in leds:                # Turns off each LED in the list in the same order
		GPIO.output(i, GPIO.LOW)
		time.sleep(delay)

# Turns on LEDs one-by-one, then turns them off in reverse order
def ReverseLine(delay):
	for i in leds:                # Turns on each LED in the list
		GPIO.output(i, GPIO.HIGH)
		time.sleep(delay)
	for i in reversed(leds):
		GPIO.output(i, GPIO.LOW)  # Turns off each LED in the list in reverse order
		time.sleep(delay)

try:
	while(True):
		Line(0.05)
except KeyboardInterrupt: # Runs until keyboard interrupt, then runs GPIO cleanup
	GPIO.cleanup()
