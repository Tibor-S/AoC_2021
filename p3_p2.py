
path = __file__ + "/../i3.in"

data = open(path).read().split()



ogr = data.copy()
csr = data.copy()

i = 0
while ogr[1:]:
  one = []
  zero = []

  for bin in ogr:
    if int(bin[i]):
      one.append(bin)
    else:
      zero.append(bin)
  
  if len(one) >= len(zero):
    ogr = one
  else:
    ogr = zero
  
  i += 1

i = 0
while csr[1:]:
  one = []
  zero = []

  for bin in csr:
    if int(bin[i]):
      one.append(bin)
    else:
      zero.append(bin)
  
  if len(one) < len(zero):
    csr = one
  else:
    csr = zero
  
  i += 1

print(ogr, csr)
print(int(ogr[0], 2) * int(csr[0], 2))
