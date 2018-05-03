import time 
import picamera 
import datetime
import RPi.GPIO as GPIO
import Adafruit_DHT


camera = picamera.PiCamera()

def relay_on():
  GPIO.setmode(GPIO.BCM) 
  GPIO.setup(17, GPIO.OUT)
  pinList = [17]
  print "IR ON"

def relay_off():
  GPIO.setup(17,GPIO.HIGH)
  GPIO.cleanup()
  print "IR OFF"


def take_pic():
         sensor1 = Adafruit_DHT.DHT11
         pin1 = 14
         humidity1, temperature1 = Adafruit_DHT.read_retry(sensor1, pin1)
         sensor2 = Adafruit_DHT.DHT11
         pin2 = 24
         humidity2, temperature2 = Adafruit_DHT.read_retry(sensor2, pin2)
	 camera.resolution = (1280, 720)
	 timestamp = (str(datetime.datetime.now()))
	 camera.annotate_text = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + (' HeatMat={0:0.1f}*C'.format(temperature1)) + (' Ambient={0:0.1f}*C'.format(temperature2))
	 time.sleep(4)
	 camera.capture("/home/pi/Gecko_main/image_bin/" + timestamp + ".jpg")
	 print "Image captured: " + timestamp

while True:
	relay_on()
	take_pic()
	relay_off()
	time.sleep(15)


