from re import match
from itertools import accumulate as acc


path = __file__ + "/../i8.in"
data = open(path).read().replace('| ', '\n').split('\n')

for i in range(len(data) // 2):
  data.pop(i)

data = list(acc(map(lambda xs: xs.split(), data), 
                lambda tot, val: tot + val))[-1]


s = 0
for seg in data:
  match len(seg):
    case 2 | 3 | 4 | 7:
      s += 1
  
print(s)

