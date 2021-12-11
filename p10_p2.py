
cStart = ['(', '[', '{', '<']
cEnd = [')', ']', '}', '>']

points = {
  ')' : 1,
  ']' : 2,
  '}' : 3,
  '>' : 4,
}

def complete(line):
  nChunk = 0
  end = ""
  tPoints = 0
  dic = {}
  for c in line:
    try:
      i = cStart.index(c)
      nChunk += 1
      dic[nChunk] = (c, cEnd[i])
    except:
      if dic[nChunk][1] != c:
        return []
      nChunk -= 1
  
  while nChunk > 0:
    tPoints *= 5
    tPoints += points[dic[nChunk][1]]
    nChunk -= 1
  
  return [tPoints]

path = __file__ + "/../i10.in"
lines = open(path).read().split()

scores = []
for line in lines:
  scores += complete(line)
  
print(sorted(scores)[len(scores) // 2])
