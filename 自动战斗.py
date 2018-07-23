from pymouse import PyMouse
import time
import random
from PIL import Image,ImageGrab
m=PyMouse()
def clicktoend():
  x=1212+random.randint(1,200)
  y=714+random.randint(-100,100)
  m.click(x,y)
  time.sleep(0.2)
  m.click(x+20,y+15)
  m.click(x-6,y-12)
  time.sleep(0.1)
  m.click(x,y)
  for i in range(5+random.randint(1,3)):
   time.sleep(0.2)
   a=random.randint(250,1000)      #随机点击的长度范围
   b=random.randint(40,600)      #随机点击的高度范围
   m.click(a,b)
  time.sleep(2.5+random.uniform(0,0.2))
  m.click(927+random.randint(-8,8),582+random.randint(-3,3))          #开始战斗的位置    
  time.sleep(1+random.uniform())
  m.click(927,582)
  time.sleep(1)
  m.click(927,582)
while 1:
  time.sleep(0.3)
  im=ImageGrab.grab()
  col=im.getpixel((452,170))   #填入判断是否战斗结束的标志的位置
  if col==(160,27,17):          #判断是否战斗结束
   clicktoend()
  else:
   pass
