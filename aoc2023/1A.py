import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true')
args = parser.parse_args()

with open("intest" if args.t else "in") as f:
  sum = 0
  for line in f.read().splitlines():
    nums = [x for x in line if x.isnumeric()]
    num = int(''.join([nums[0], nums[-1]]))
    sum += num

  print(sum)
