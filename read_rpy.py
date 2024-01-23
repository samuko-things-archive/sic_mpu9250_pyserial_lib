from sic_pyserial_lib import SIC
import time


imu = SIC('/dev/ttyUSB0')


for i in range(30):
  time.sleep(1.0)
  print(i+1, " sec")

prevTime = time.time()
sampleTime = 0.05
while True:

  if time.time() - prevTime > sampleTime:
    try:
      roll, pitch, yaw = imu.getRPY() #without heading

      # yaw = imu.getHeading # with heading

      print(f"roll: {roll}, pitch: {pitch}, yaw: {yaw}")
      print("")
    except:
      pass
    
    prevTime = time.time()

