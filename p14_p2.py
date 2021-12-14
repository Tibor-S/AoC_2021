 
 
path = __file__ + "/../i14.in"
data = open(path).read().replace('->', ' ').split()
count = [0 for i in range(ord('Z') - ord('A'))]
rules = {}
while data[1:]:
  to = data.pop()
  key = data.pop()
  rules[key] = {"to": [key[0] + to, to + key[1]], "current": 0, "next": 0}
for i in range(len(data[0]) - 1): 
  count[ord(data[0][i]) - 65] += 1
  rules[data[0][i:i+2:]]["current"] += 1
count[ord(data[0][-1]) - 65] += 1


for n in range(40):
  for key in rules:
    count[ord(rules[key]["to"][0][1]) - 65] += rules[key]["current"]
    for to in rules[key]["to"]:
      rules[to]["next"] += rules[key]["current"]
    rules[key]["current"] = 0
  for key in rules:
    rules[key]["current"] = rules[key]["next"]
    rules[key]["next"] = 0
count = sorted([c for c in count if c != 0])
print(count[-1] - count[0])