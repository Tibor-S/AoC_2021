from collections import defaultdict as dd
 
path = __file__ + "/../i13.in"
data = open(path).read().split('\n')
paper = []
inst = []

while data[-1] != '':
  i = data.pop().split()[-1].split('=')
  inst.append((i[0], int(i[1])))
data.pop()
inst.reverse()

for c in data:
  c = c.split(',')
  paper.append((int(c[0]), int(c[1])))

for i in inst[:1]:
  for j in range(len(paper)):
    c = paper.pop(0)
    match i[0]:
      case 'x':
        paper.append((i[1] - abs(i[1] - c[0]), c[1]))
      case 'y':
        paper.append((c[0], i[1] - abs(i[1] - c[1])))
        
  paper = list(set(paper))   

print(len(paper))
