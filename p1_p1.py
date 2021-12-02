
path = __file__ + "/../i1.in"

data = open(path).read().split()

x = int(data.pop(0))

c = 0
for xs in data:
  nx = int(xs)
  if nx > x: c += 1
  x = nx

print(c)