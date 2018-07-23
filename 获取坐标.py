import time
from pymouse import PyMouse

m=PyMouse()
time.sleep(1)
print(m.position())
