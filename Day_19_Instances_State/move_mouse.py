import  mouse
import random

x = random.randint(0,10)
y = random.randint(1,11)

mouse_move = True
count = 0

while mouse_move:
    
    if count < 500000:
        mouse.move(x,y)
        print (count)
        count += 1
    else:
        mouse_move = False

    


