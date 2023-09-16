import math

with open("in") as f:
    X = 1
    cycle = 0
    rows = [['.' for _ in range(40)] for _ in range(6)]

    for line in f.read().splitlines():
        if 'addx' in line:
            cycle += 1

            if X - 1 <= cycle % 40 <= X + 1:
                rows[math.floor(cycle / 40)][cycle % 40] = 'X'

            V = int(line.split()[-1])
            X += V

        cycle += 1

        if X - 1 <= cycle % 40 <= X + 1:
            rows[math.floor(cycle / 40)][cycle % 40] = 'X'

    for r in rows:
        print(''.join(r))
