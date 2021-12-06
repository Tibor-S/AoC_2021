days = 80
path = __file__ + "/../i6.in"
school = list(map(int, open(path).read().split(',')))

for i in range(days):
  nSchool = []
  while school:
    fish = school.pop()
    if fish == 0:
      nSchool.append(6)
      nSchool.append(8)
    else:
      nSchool.append(fish - 1)
  school = nSchool

print(len(school))