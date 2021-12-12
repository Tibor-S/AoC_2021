from collections import defaultdict as dd
 
path = __file__ + "/../i12.in"
data = list(map(lambda str: str.split('-'), open(path).read().split()))
tree = dd(lambda: [])

for conn in data:
  tree[conn[0]].append(conn[1])
  tree[conn[1]].append(conn[0])
tree['end'] = []

paths = [['start']]
while not sum(map(lambda arr: arr[-1] == 'end', paths)) == len(paths):
  for i in range(len(paths)):
    path = paths.pop(0)
    if path[-1] == 'end':
      paths.append(path)
    else:
      for cave in tree[path[-1]]:
        # print(cave)
        if cave.islower():
          if path.__contains__(cave) == False:
            paths.append(path + [cave])
        elif cave.isupper():
          paths.append(path + [cave])

print(len(paths))