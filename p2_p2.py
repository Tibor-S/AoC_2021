path = __file__ + "/../i2.in"

data = open(path).read().split()

pos = 0
dep = 0
aim = 0
while data:
  inst = data.pop(0)
  val = data.pop(0)

  match inst:
    case 'forward':
      pos += int(val)
      dep += aim * int(val)
    case 'up':
      aim -= int(val)
    case 'down':
      aim += int(val)

print (pos * dep)
