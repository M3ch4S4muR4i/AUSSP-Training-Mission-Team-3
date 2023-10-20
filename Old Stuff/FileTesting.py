filename = 'UsefulData.txt'
file = open(filename, 'a')
file.write("This is text. \n")
file.write(['x_acc','y_acc','z_acc','x_ang_vel','y_ang_vel','z_ang_vel','temp','pres'])
file.close()