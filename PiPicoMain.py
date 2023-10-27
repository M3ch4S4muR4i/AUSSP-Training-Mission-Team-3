from imu import MPU6050
from bmp085 import BMP180
from machine import Pin, I2C
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1))        
imu = MPU6050(i2c)
bmp = BMP180(i2c)
bmp.oversample = 2
bmp.sealevel = 1022.6

# Create file
file = open('Data.txt', "w")
file.write("time,xa,xy,xz,xav,yav,zav,temp,pressure\n")
file.close()
print("Readings from MPU6050 and BMP180\n\ntime\txa\txy\txz\txav\tyav\tzav\ttemp\tpressure\n")


# delay start?
#time.sleep(20)


# timer
startTime = time.ticks_ms()
    
while True:
    # MPU6050 readings
    x_accel = imu.accel.x
    y_accel = imu.accel.y
    z_accel = imu.accel.z
    x_ang_vel = imu.gyro.x
    y_ang_vel = imu.gyro.y
    z_ang_vel = imu.gyro.z
    #temperature = imu.temperature #theoretically better from bmp than mpu

    
    
    # BMP180 readings
    #need to find out how to get these readings
    temperature = bmp.temperature #temp in celsius
    pressure = bmp.pressure #pressure in hPa
    #altitude = bmp.altitude
    #pressure = 0.0
    #temperature = 0.0 #theoretically better from bmp than mpu
    
    
    # Readings to string    
    xa = '{:014.10f}'.format(x_accel)
    ya = '{:014.10f}'.format(y_accel)
    za = '{:014.10f}'.format(z_accel)
    xav= '{:014.10f}'.format(x_ang_vel)
    yav= '{:014.10f}'.format(y_ang_vel)
    zav= '{:014.10f}'.format(z_ang_vel)
    tmp= '{:014.10f}'.format(temperature)
    prs= '{:014.10f}'.format(pressure)
    
    
    # timer continued
    endTime = time.ticks_ms()
    timeOfReading = (endTime - startTime) / 1000
    stringTime = '{:2.3f}'.format(timeOfReading)
    
    
    
    # Organize data
    mpuValues = '{}, {}, {}, {}, {}, {}'.format(xa, ya, za, xav, yav, zav)
    printable = "{}, {}, {}, {}".format(stringTime, mpuValues, tmp, prs)


    # Add to file
    file = open("Data.txt", "a")
    file.write(printable + '\n')
    file.close()
    print("{} {} {} {}".format(stringTime, mpuValues, tmp, prs))
    
    
    # buffer time
    time.sleep(0.2)
