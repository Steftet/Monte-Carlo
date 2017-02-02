import math
import random
import canvas

f = 200
h = 0

canvas.set_size(f, f)
canvas.set_fill_color(1, 1, 1)
canvas.fill_rect(0,0,f,f)

k = int(input('Anzahl Punkte: '))
for i in range(0,k):
    x = (random.randint(0,f)/f)
    y = (random.randint(0,f)/f)
    if math.sqrt(math.pow(x,2)+math.pow(y,2))<=1:
    	h+=1
    	canvas.set_fill_color(0,1,0)
    	canvas.fill_pixel(x*f,y*f)
    else:
    	canvas.set_fill_color(1,0,0)
    	canvas.fill_pixel(x*f,y*f)
    	
    if i%5000 == 0:
   		print(i)

print(h/k)