with open("in") as f:
  H = [0, 0]
  T = [0, 0]
  visited = [[0, 0]]
  for line in f.read().splitlines():
    direction, steps = line.split()
    for i in range(int(steps)):
      if direction == 'R':
        H[0] += 1
      elif direction == 'L':
        H[0] -= 1
      elif direction == 'U':
        H[1] += 1
      elif direction == 'D':
        H[1] -= 1

      # Tail mechanics
      adj = [
        [T[0] + dx, T[1] + dy]
        for dx in [-1, 0, 1]
        for dy in [-1, 0, 1]
        if dx != 0 or dy != 0
      ]

      if H not in adj:
        if H[0] > T[0] and H[1] == T[1]:  # right
          T[0] += 1
        elif H[0] < T[0] and H[1] == T[1]:  # left
          T[0] -= 1
        elif H[0] == T[0] and H[1] > T[1]:  # up
          T[1] += 1
        elif H[0] == T[0] and H[1] < T[1]:  # down
          T[1] -= 1
        elif H[0] > T[0] and H[1] > T[1]:  # up right
          T[0] += 1
          T[1] += 1
        elif H[0] < T[0] and H[1] > T[1]:  # down right
          T[0] -= 1
          T[1] += 1
        elif H[0] < T[0] and H[1] < T[1]:  # down left
          T[0] -= 1
          T[1] -= 1
        elif H[0] > T[0] and H[1] < T[1]:  # down right
          T[0] += 1
          T[1] -= 1

      # print(f"{H} {T}")
      # Check if visited
      if T not in visited:
        visited.append(T.copy())

  # print(visited)
  print(len(visited))
