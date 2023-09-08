total = 0

with open("in") as f:
  for line in f.read().splitlines():
    groups = line.split(sep=',')
    group1 = list(map(int, groups[0].split(sep='-')))
    group2 = list(map(int, groups[1].split(sep='-')))
    range1 = [x for x in range(group1[0], group1[1] + 1)]
    range2 = [x for x in range(group2[0], group2[1] + 1)]
    if (any(x in range1 for x in range2)) or (any(x in range2 for x in range1)):
      total += 1

print(total)
