from itertools import accumulate as acc

path = __file__ + "/../i3.in"

data = open(path).read().split()

def lol(binary, count):
  for b in binary:
    if b == '1':
      count.append(count.pop(0) + 1)
    else:
      count.append(count.pop(0) - 1)
  
  return count

c = [0 for i in range(len(data[0]))]
g = ""
e = ""

while data:
  lol(data.pop(0), c)

for i in range(len(c)):
  if c.pop(0) >= 0:
    g += '1'
    e += '0'
  else:
    g += '0'
    e += '1'



print(int(e, 2) * int(g, 2))