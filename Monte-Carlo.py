import math
import random

h = 0

k = int(input('Number of dots: '))
for i in range(0,k):
    x = (random.randint(0,100)/100)
    y = (random.randint(0,100)/100)
    if math.sqrt(math.pow(x,2)+math.pow(y,2))<=1:
        h+=1

print(h/k)
