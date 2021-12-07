path = __file__ + "/../i7.in"
data = list(map(int, open(path).read().split(',')))
data.sort()

ls = sum(map(lambda x: (abs(x) + 1) * (x)/2, data))
for t in range(1, data[-1] + 1):
  s = sum(map(lambda x: int((abs(x - t)) * (abs(x - t) + 1)/2), data))
  if s < ls:
    ls = s
  else:
    break

print(ls)

