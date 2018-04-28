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
	 sensor = Adafruit_DHT.DHT11
 	 pin = 14
  	 humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	 camera.resolution = (1280, 720)
	 timestamp = (str(datetime.datetime.now()))
	 camera.annotate_text = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + (' HeatMat={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
	 time.sleep(4)
	 camera.capture("/home/pi/Gecko_main/image_bin/" + timestamp + ".jpg")
	 print "Image captured: " + timestamp

while True:
	relay_on()
	take_pic()
	relay_off()
	time.sleep(15)


