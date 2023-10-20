from machine import I2C, PIN
import time

# MPU6050 i2c address: 0x68
# BMP180 i2c address: 0x77

SDA = Pin(16)
SCL = Pin(17)
i2c = I2C(id=0, SDA, SCL)

# Create file
file = open('Data.txt', 'w')
file.write("Readings from MPU6050 and BMP180", 'a')


while True:
    # timer
    startTime = time.time()
    
    
    # MPU6050 readings
    x_accel = i2c.readfrom_mem(0x68, 0x3B, 2)
    y_accel = i2c.readfrom_mem(0x68, 0x3C, 2)
    z_accel = i2c.readfrom_mem(0x68, 0x3D, 2)
    x_ang_vel = i2c.readfrom_mem(0x68, 0x43, 2)
    y_ang_vel = i2c.readfrom_mem(0x68, 0x45, 2)
    z_ang_vel = i2c.readfrom_mem(0x68, 0x47, 2)
    temperature = i2c.readfrom_mem(0x68, 0x41, 2)


    # BMP180 readings
    pressure = i2c.readfrom_mem(0x77, 0xF7, 2)
    
    
    # timer continued
    endTime = time.time()
    timeOfReading = endTime - startTime
    formatted_timeOfReading = f'{timeOfReading:07.3f}'
    
    
    # Add to file
    values = [x_accel, y_accel, z_accel, x_ang_vel, y_ang_vel, z_ang_vel]
    formatted_values = [f'{value:010.6f}' for value in values]
    data = "{}: {}".format(formatted_timeOfReading, formatted_values)
    file.write(data, 'a')
    file.close()
    
