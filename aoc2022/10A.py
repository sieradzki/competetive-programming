with open("in") as f:
  X = 1
  cycle = 1
  ss = {}
  for line in f.read().splitlines():
    if 'addx' in line:
      cycle += 1

      if cycle == 20 or (cycle - 20) % 40 == 0:
        ss[cycle] = cycle * X

      V = int(line.split()[-1])
      X += V

    cycle += 1
    if cycle == 20 or (cycle - 20) % 40 == 0:
      ss[cycle] = cycle * X

  print(sum(ss.values()))
