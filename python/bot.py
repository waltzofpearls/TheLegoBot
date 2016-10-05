from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_ULTRASONIC_CONT
BrickPiSetupSensors()

while True:
  result = BrickPiUpdateValues()
  if not result:
    print BrickPi.Sensor[PORT_1]
  time.sleep(.01)
