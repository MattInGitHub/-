from pymouse import PyMouse
import time

m=PyMouse()
time.sleep(3)
for i in range(6):
 time.sleep(0.004)
 m.click(526,180)
time.sleep(1)
m.move(943,200)
time.sleep(0.5)
m.drag(557,17)
time.sleep(1)
m.move(1243,203)
time.sleep(0.5)
m.drag(1674,367)