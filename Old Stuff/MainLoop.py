from machine import I2C, Pin
# MPU6050 0x68
# BMP180  0x77
# ACCEL_XOUT_H  is 3B
# ACCEL_YOUT_H  is 3D
# ACCEL_ZOUT_H  is 3F
# GYRO_XOUT_H is 43
# GYRO_YOUT_H is 45
# GYRO_ZOUT_H is 47
sda = Pin(16)
scl = Pin(17)
i2c = I2C(id = 0, Sda = Sda, SCL = SCL)
filename = 'FlightData.txt'
file = open(filename, 'a')
file.write('\n New Flight \n\n')

while True:
    file = open(filename, 'a')
    x_acc = i2c.readfrom_mem(0x68, 0x3B, 2) # accel x
    y_acc = i2c.readfrom_mem(0x68, 0x3D, 2) # accel y
    z_acc = i2c.readfrom_mem(0x68, 0x3F, 2) # accel z
    x_ang_vel = i2c.readfrom_mem(0x68, 0x43, 2) # gyro x
    y_ang_vel = i2c.readfrom_mem(0x68, 0x45, 2) # gyro y
    z_ang_vel = i2c.readfrom_mem(0x68, 0x47, 2) # gyro z
    temp = i2c.readfrom_mem(0x68, 0x41, 2) # temperature
    pres = i2c.readfrom_mem(0x77, 0xF7, 2) # pressure
    
    #data_list = [x_acc,y_acc,z_acc,x_ang_vel,y_ang_vel,z_ang_vel,temp,pres]
    
    file.write("{} {} {} {} {} {} {} {}",x_acc,y_acc,z_acc,x_ang_vel,y_ang_vel,z_ang_vel,temp,pres)
    file.close()




