days = 256
path = __file__ + "/../i6.in"
school = [0 for i in range(9)]
for i in open(path).read().split(','): school[int(i)] += 1

for d in range(days):
  nS = [0 for i in range(9)]
  for i in range(1,9):
    nS[i-1] += school[i]
  nS[6] += school[0]
  nS[8] += school[0]
  school = nS
  
print(sum(school))