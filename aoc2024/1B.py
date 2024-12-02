import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true')
args = parser.parse_args()

with open("intest" if args.t else "in") as f:
  l1, l2 = [], []
  for line in f.read().splitlines():
    n1, n2 = [int(x) for x in line.split()]
    l1.append(n1)
    l2.append(n2)

  l1.sort()
  l2.sort()

  sum = 0
  for i, x in enumerate(l1):
    cnts = l2.count(x)
    sum += x * cnts

  print(sum)
