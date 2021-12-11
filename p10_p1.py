
cStart = ['(', '[', '{', '<']
cEnd = [')', ']', '}', '>']

points = {
  ')' : 3,
  ']' : 57,
  '}' : 1197,
  '>' : 25137,
}

def isCor(line):
  nChunk = 0
  dic = {}
  for c in line:
    try:
      i = cStart.index(c)
      nChunk += 1
      dic[nChunk] = (c, cEnd[i])
    except:
      if dic[nChunk][1] != c:
        return points[c]
      nChunk -= 1
  return 0
    

path = __file__ + "/../i10.in"
lines = open(path).read().split()

sum = 0
for line in lines:
  sum += isCor(line)
print(sum)