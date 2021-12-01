
path = __file__ + "/../i1.txt"

data = list(map(lambda xs: int(xs), open(path).read().split()))

x = data.pop(0)

c = 0
while True:
  try:
    ms = data[:3]
    nx = sum(ms)
    if nx > x and len(ms) == 3:
      c += 1
    x = nx
    data.pop(0)
  except:
    break

print(c)
