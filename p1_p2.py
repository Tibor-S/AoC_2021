
path = __file__ + "/../i1.in"

data = list(map(lambda xs: int(xs), open(path).read().split()))

x = data[-1]

c = 0
while data:
  nx = sum(data[:3])
  if nx > x: c += 1
  x = nx
  data.pop(0)

print(c)
