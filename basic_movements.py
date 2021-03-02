from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

me.takeoff()
# Key for RC controls (0 Right -0 Left, 0 Forward -0 Backwards, 0 Yaw Right, -0 Yaw Left)
me.send_rc_control(0, 0, 10, 0)
sleep(2)


me.land
