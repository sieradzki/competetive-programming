with open("in") as f:
  totals = []
  sm = 0
  for x in f.readlines():
    x = x.strip()
    if x != '':
      sm += int(x)
    else:
      totals.append(sm)
      sm = 0

print(sum(sorted(totals, reverse=True)[:3]))
