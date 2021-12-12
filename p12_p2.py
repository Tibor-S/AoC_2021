from collections import defaultdict as dd
 
path = __file__ + "/../i12.in"
data = list(map(lambda str: str.split('-'), open(path).read().split()))
tree = dd(lambda: [])

for conn in data:
  tree[conn[0]].append(conn[1])
  tree[conn[1]].append(conn[0])
tree['end'] = []

paths = [[2, 'start']]
while not sum(map(lambda arr: arr[-1] == 'end', paths)) == len(paths):
  for i in range(len(paths)):
    path = paths.pop(0)
    if path[-1] == 'end':
      paths.append(path)
    else:
      for cave in tree[path[-1]]:
        # print(cave)
        if cave == 'start': continue
        elif cave == 'end': 
          # print('____________________________')
          # print(path + [cave])
          # print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
          paths.append(path + [cave])
        elif cave.islower():
          c = path.count(cave)
          if c < path[0]:
            if path[0] > 1 and c > 0: paths.append([path[0] - 1] + path[1:] + [cave])
            else: paths.append(path + [cave])
        elif cave.isupper(): paths.append(path + [cave])
print(len(paths))