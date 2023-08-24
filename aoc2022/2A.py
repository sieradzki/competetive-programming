with open("in") as f:
  score = 0
  d = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
  for line in f.readlines():
    a, b = line.split()
    x, y = d[a], d[b]
    if x == y:
      score += 3
    elif (x == 1 and y == 2) or (x == 2 and y == 3) or (x == 3 and y == 1):
      score += 6
    score += y

print(score)
