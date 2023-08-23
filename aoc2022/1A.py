with open("inputs/1A") as f:
  mx = 0
  sm = 0
  for x in f.readlines():
    x = x.strip()
    if x != '':
      sm += int(x)
    else:
      if sm > mx:
        mx = sm
      sm = 0

  print(mx)
