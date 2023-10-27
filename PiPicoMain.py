from imu import MPU6050
from time import sleep
from machine import Pin, I2C

i2c = I2C(1, sda=Pin(2), scl=Pin(3))
imu = MPU6050(i2c)

while True:
    # MPU6050 readings
    x_accel = imu.accel.x
    y_accel = imu.accel.y
    z_accel = imu.accel.z
    x_ang_vel = imu.gyro.x
    y_ang_vel = imu.gyro.y
    z_ang_vel = imu.gyro.z
    temperature = imu.temperature
    print(x_accel, y_ang_vel, temperature)
    sleep(0.2)
