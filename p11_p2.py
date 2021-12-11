from math import nan, sin, cos, pi
from collections import defaultdict as dd

path = __file__ + "/../i11.in"
data = open(path).read().split()
sX = len(data[0])
sY = len(data)
grid = dd(lambda: nan)
reset = []

for y in range(len(data)):
  for x in range(len(data[y])): grid[x, y] = int(data[y][x])
  
def flash(x, y):
  reset.append((x,y))
  for v in range(8): 
    x1 = round(x + cos(2 * v * pi / 8))
    y1 = round(y + sin(2 * v * pi / 8))
    
    grid[x1, y1] += 1
    if grid[x1, y1] == 10:
      flash(x1, y1)

def main(n):
  step = 1
  while True:
    for x in range(sX):
      for y in range(sY):
        # print(x,y)
        grid[x,y] += 1
        if grid[x,y] == 10:
          flash(x,y)
    if len(reset) == sX * sY: 
      print(step)
      break
    for r in reset: grid[r] = 0
    reset.clear()
    step += 1
      
main(1)
