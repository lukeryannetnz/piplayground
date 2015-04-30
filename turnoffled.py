try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO! Try running as su")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

# while True:
GPIO.output(4, GPIO.LOW)

#GPIO.cleanup()
