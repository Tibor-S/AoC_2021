from collections import defaultdict as dd
from itertools import accumulate as acc

path = __file__ + "/../i9.in"
data = list(map(lambda xs: [9] + list(map(int, list(xs))) + [9], open(path).read().split()))
data = [[9 for i in data[0]]] + data + [[9 for i in data[0]]]


def surround(x, y, grid):
  surr = []
  cand = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
  # print(x, y, cand)
  for i in cand:
    if grid[i] and data[i[1]][i[0]] - data[y][x] > 0 and data[i[1]][i[0]] != 9:
      surr.append(i)
      grid[i] = False
      # print(surr)
      for j in surr: surr += surround(j[0], j[1],grid)
      
  return surr
  
basin = []
for y in range(1, len(data) - 1): 
  for x in range(1, len(data[0]) - 1):
    grid = dd(lambda: True)
    if data[y][x-1] > data[y][x] and data[y][x+1] > data[y][x] and data[y+1][x] > data[y][x] and data[y-1][x] > data[y][x]:
      basin.append(1 + len(surround(x, y, grid)))
      
      
print(list(acc(sorted(basin)[-3:], lambda t, v: t*v))[-1])