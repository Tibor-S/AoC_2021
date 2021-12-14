 
 
path = __file__ + "/../i14.in"
data = open(path).read().replace('->', ' ').split()
count = [0 for i in range(ord('Z') - ord('A'))]
rules = {}
while data[1:]:
  rules[data.pop()] = data.pop()
polymer = list(data.pop())
for n in range(10):
  for i in range(len(polymer) - 1):
    polymer.append(polymer.pop(0))
    polymer.append(rules[polymer[-1] + polymer[0]])
  polymer.append(polymer.pop(0))
for c in polymer: count[ord(c) - 65] += 1
count = sorted([c for c in count if c != 0])
print(count[-1] - count[0])