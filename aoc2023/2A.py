import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true')
args = parser.parse_args()

with open("intest" if args.t else "in") as f:
  sum_ids = 0
  for line in f.read().splitlines():
    game_id = int(line.split()[1][:-1])
    line = line.split(sep=':')[1]
    possible = True
    for set in line.split(sep=';'):
      if not possible:
        break
      for cubes in set.split(sep=','):
        num = int(cubes.split()[0])
        color = cubes.split()[1].strip()
        if 'red' in color and num > 12:
          possible = False
        elif 'green' in color and num > 13:
          possible = False
        elif 'blue' in color and num > 14:
          possible = False
    if (possible):
      sum_ids += game_id

  print(sum_ids)
