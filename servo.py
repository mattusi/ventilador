from time import sleep
import RPi.GPIO as GPIO

class Servo(object):

    def __init__(self, gpioPin):
        self.gpioPin = gpioPin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(gpioPin, GPIO.OUT)
        self.pwm = GPIO.PWM(gpioPin, 50)
        self.pwm.start(0)

    def setAngle(self, angle):
        duty = angle / 18 + 2
        GPIO.output(self.gpioPin, True)
        self.pwm.ChangeDutyCycle(duty)
        sleep(1.5)
        GPIO.output(self.gpioPin, False)
        self.pwm.ChangeDutyCycle(0)

servo = Servo(7)
while True:
    angle = int(input("entre um angulo:"))
    servo.setAngle(angle)
    