import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true')
args = parser.parse_args()

with open("intest" if args.t else "in") as f:
  sum = 0
  for line in f.read().splitlines():
    nums = [int(x) for x in line.split()]
    inc = nums[1] - nums[0] > 0
    safe = True
    for i in range(len(nums) - 1):
      if not safe:
        break
      diff = nums[i + 1] - nums[i]
      if not (abs(diff) in range(1, 4)) or ((diff < 0 and inc) or (diff > 0 and not inc)):
        safe = False

    if safe:
      sum += 1

  print(sum)
