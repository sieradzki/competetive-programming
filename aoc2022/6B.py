with open("in") as f:
  data = f.read()
  beg = 0
  end = 14
  while (True):
    if len(set(data[beg:end])) == len(data[beg:end]):
      print(end)
      break
    beg += 1
    end += 1
