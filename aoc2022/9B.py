with open("in") as f:
  K = [[0, 0] for i in range(10)]  # Head is now K[0]
  visited = [[0, 0]]
  for line in f.read().splitlines():
    direction, steps = line.split()
    for i in range(int(steps)):
      if direction == 'R':
        K[0][0] += 1
      elif direction == 'L':
        K[0][0] -= 1
      elif direction == 'U':
        K[0][1] += 1
      elif direction == 'D':
        K[0][1] -= 1
      for j in range(1, 10):
        # Tail mechanics
        adj = [
          [K[j][0] + dx, K[j][1] + dy]
          for dx in [-1, 0, 1]
          for dy in [-1, 0, 1]
          if dx != 0 or dy != 0
        ]

        if K[j - 1] not in adj:
          if K[j - 1][0] > K[j][0] and K[j - 1][1] == K[j][1]:  # right
            K[j][0] += 1
          elif K[j - 1][0] < K[j][0] and K[j - 1][1] == K[j][1]:  # left
            K[j][0] -= 1
          elif K[j - 1][0] == K[j][0] and K[j - 1][1] > K[j][1]:  # up
            K[j][1] += 1
          elif K[j - 1][0] == K[j][0] and K[j - 1][1] < K[j][1]:  # down
            K[j][1] -= 1
          elif K[j - 1][0] > K[j][0] and K[j - 1][1] > K[j][1]:  # up right
            K[j][0] += 1
            K[j][1] += 1
          elif K[j - 1][0] < K[j][0] and K[j - 1][1] > K[j][1]:  # down right
            K[j][0] -= 1
            K[j][1] += 1
          elif K[j - 1][0] < K[j][0] and K[j - 1][1] < K[j][1]:  # down left
            K[j][0] -= 1
            K[j][1] -= 1
          elif K[j - 1][0] > K[j][0] and K[j - 1][1] < K[j][1]:  # down right
            K[j][0] += 1
            K[j][1] -= 1

      if K[-1] not in visited:
        visited.append(K[-1].copy())

  # print(visited)
  print(len(visited))
