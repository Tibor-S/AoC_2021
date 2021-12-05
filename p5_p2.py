from collections import defaultdict as dd

path = __file__ + "/../i5.in"
pipes = list(map(lambda xs: (tuple(map(int, xs[0].split(','))), tuple(map(int, xs[1].split(',')))), map(lambda xs: xs.split(' -> '), open(path).read().split('\n'))))
grid = {}
grid = dd(lambda: 0)

for pipe in pipes:
  strt = pipe[0]
  end = pipe[1]
  if strt[0] == end[0] or strt[1] == end[1]:
    for x in range(min(strt[0], end[0]), max(strt[0], end[0]) + 1):
      for y in range(min(strt[1], end[1]), max(strt[1], end[1]) + 1):
        grid[(x,y)] += 1
  else:
    dir = ((end[0] - strt[0]) // abs(end[0] - strt[0]), (end[1] - strt[1]) // abs(end[1] - strt[1]))
    for i in range(abs(strt[0] - end[0]) + 1):
      grid[(strt[0] + i * dir[0], strt[1] + i * dir[1])] += 1

c = 0    
for key in grid:
  if grid[key] > 1:
    c += 1

print(c)