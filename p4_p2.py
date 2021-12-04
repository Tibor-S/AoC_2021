from itertools import accumulate as acc
from math import floor as flr

path = __file__ + "/../i4.in"
data = open(path).read().split()
boards = []
bingo = list(map(int,data.pop(0).split(',')))
size = 5
# init
while data:
  boards.append([[int(data.pop(0)) for x in range(5)] for y in range(5)])

def lol(s, n):
  if n == 100: return s
  return s + n

def sumB(board):
  return sum([n % 100 for n in list(acc(board, lambda tot, val: tot + val))[-1]])

def main(boards):
  for num in bingo:
    nBoards = boards.copy()
    for i in range(len(nBoards)):
      done = False
      board = nBoards.pop(0)
      cols = [[] for i in range(size)]
      
      #rows
      for row in board:
        for i in row:
          n = row.pop(0)
          cols[0].append(n)
          cols.append(cols.pop(0))
          if n == num:
            row.append(100)
          else:
            row.append(n)
        if sum(row) == size * 100:
          if len(boards) == 1:
            return sumB(board) * num
          else:
            done = True
      #cols
      for col in cols:
        for i in col:
          n = col.pop(0)
          if n == num:
            col.append(100)
          else:
            col.append(n)
        if sum(col) == size * 100:
          if len(boards) == 1:
            return sumB(board) * num
          else:
            done = True
      
      if not done:
        nBoards.append(board)
    boards = nBoards
      

print(main(boards))
          