import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true')
args = parser.parse_args()

with open("intest" if args.t else "in") as f:
  sum = 0
  for line in f.read().splitlines():
    game_id = int(line.split()[1][:-1])
    line = line.split(sep=':')[1]
    max_red = 1
    max_green = 1
    max_blue = 1
    for set in line.split(sep=';'):
      for cubes in set.split(sep=','):
        num = int(cubes.split()[0])
        color = cubes.split()[1].strip()
        if 'red' in color and num > max_red:
          max_red = num
        elif 'green' in color and num > max_green:
          max_green = num
        elif 'blue' in color and num > max_blue:
          max_blue = num
    power = max_red * max_green * max_blue
    sum += power
  print(sum)
