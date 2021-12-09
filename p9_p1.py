
 
path = __file__ + "/../i9.in"
data = list(map(lambda xs: [10] + list(map(int, list(xs))) + [10], open(path).read().split()))
data = [[10 for i in data[0]]] + data + [[10 for i in data[0]]]
sum = 0

for y in range(len(data)): 
  for x in range(len(data[0])):
    if data[y][x-1] > data[y][x] and data[y][x+1] > data[y][x] and data[y+1][x] > data[y][x] and data[y-1][x] > data[y][x]:
      sum += 1 + data[y][x]
      
print(sum)