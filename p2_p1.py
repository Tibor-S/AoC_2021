path = __file__ + "/../i2.in"

data = open(path).read().split()

pos = 0
dep = 0
while data:
  inst = data.pop(0)
  val = data.pop(0)

  match inst:
    case 'forward':
      pos += int(val)
    case 'up':
      dep -= int(val)
    case 'down':
      dep += int(val)

print (pos * dep)

