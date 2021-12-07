path = __file__ + "/../i7.in"
data = list(map(int, open(path).read().split(',')))
data.sort()
ls = sum(data)

for t in range(1, data[-1] + 1):
  s = sum(map(lambda x: abs(x - t), data))
  if s < ls:
    ls = s
  else:
    break

print(ls)

