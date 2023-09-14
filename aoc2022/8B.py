with open("in") as f:
  trees = []
  for line in f.read().splitlines():
    row = [int(tree) for tree in line]
    trees.append(row)

  s_scores = []
  for x, row in enumerate(trees):
    for y, tree in enumerate(row):
      if x == 0 or x == len(trees) - 1 or y == 0 or y == len(trees) - 1:
        continue

      v_dists = []
      dist = 0
      for item in row[:y][::-1]:
        dist += 1
        if item >= tree:
          break
      v_dists.append(dist)

      dist = 0
      for item in row[y + 1:]:
        dist += 1
        if item >= tree:
          break
      v_dists.append(dist)

      dist = 0
      column = [row[y] for row in trees]
      for item in column[:x][::-1]:
        dist += 1
        if item >= tree:
          break
      v_dists.append(dist)

      dist = 0
      for item in column[x + 1:]:
        dist += 1
        if item >= tree:
          break
      v_dists.append(dist)

      ss = 1
      for v_dist in v_dists:
        ss *= v_dist

      s_scores.append(ss)

  print(max(s_scores))
