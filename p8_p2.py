from collections import defaultdict as dd
from itertools import accumulate as acc, permutations as perms

tmp = True

toSeg = {
  '0' : 'abcefg',
  '1' : 'cf',
  '2' : 'acdeg',
  '3' : 'acdfg',
  '4' : 'bcdf',
  '5' : 'abdfg',
  '6' : 'abdefg',
  '7' : 'acf',
  '8' : 'abcdefg',
  '9' : 'abcdfg',
}
toNum = {}
for key in toSeg: toNum[toSeg[key]] = key
path = __file__ + "/../i8.in"
data = open(path).read().replace('| ', '\n').split('\n')
data = list(map(lambda str: str.split(), data))


s = 0
while data:
  input = data.pop(0)
  output = data.pop(0)
  wires = 'abcdefg'
  segments = list(perms('abcdefg', len('abcdefg')))
  for seg in segments:
    rel = {}
    for i in range(7):
      rel[wires[i]] = seg[i]
    
    done = True
    for dig in input:
      nDig = ''
      for c in dig: nDig += rel[c]
      try:
        toNum[''.join(sorted(nDig))]
      except:
        done = False
        break
    
    if done:
      out = int(''.join([toNum[''.join(sorted([rel[c] for c in d]))] for d in output]))
      s += out
      break
  
    
    
  
print(s)

