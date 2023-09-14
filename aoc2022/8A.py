with open("in") as f:
  trees = []
  for line in f.read().splitlines():
    row = [int(tree) for tree in line]
    trees.append(row)

  visible = 0
  for x, row in enumerate(trees):
    for y, tree in enumerate(row):
      if x == 0 or x == len(trees) - 1 or y == 0 or y == len(trees) - 1:
        visible += 1
      else:
        # check in a row
        if tree > max(row[:y]) or tree > max(row[y + 1:]):
          visible += 1
          continue

        # column
        column = [row[y] for row in trees]
        if tree > max(column[:x]) or tree > max(column[x + 1:]):
          visible += 1

  print(visible)

  # print(trees)
