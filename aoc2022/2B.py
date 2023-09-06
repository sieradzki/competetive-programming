with open("in") as f:
  score = 0
  d = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
  for line in f.readlines():
    a, b = line.split()
    x, y = d[a], d[b]
    if y == 1:  # lose
      score += 3 if x == 1 else 1 if x == 2 else 2
    elif y == 2:  # draw
      score += x + 3
    elif y == 3:  # win
      score += (2 if x == 1 else 3 if x == 2 else 1) + 6

print(score)
