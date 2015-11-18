import RPi.GPIO as GPIO
import signal
import sys
import time

gpio_leds = { 'green' : 6, 'yellow1' : 19, 'yellow2' : 13, 'red' : 26 }

def boardConfiguration():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

def gpio_configuration(gpio):
    GPIO.setup(gpio, GPIO.OUT)

def closeValv():
    print "valv close"
    GPIO.output(valvgpio, 0)
    GPIO.cleanup()

def led_on(led_name):
    led_gpio = gpio_leds.get(led_name)
    GPIO.output(led_gpio, 1)

def led_off(led_name):
    led_gpio = gpio_leds.get(led_name)
    GPIO.output(led_gpio, 0)


# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)



boardConfiguration()
print "transaction: start"

for led in gpio_leds.values():
    gpio_configuration(led)

for led_name in gpio_leds.keys():
    led_on(led_name)
    time.sleep(0.5)

time.sleep(2)

for led_name in list(reversed(gpio_leds.keys())):
    led_off(led_name)
    time.sleep(0.5)
