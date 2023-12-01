import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true')
args = parser.parse_args()

digits = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9
}

with open("intest" if args.t else "in") as f:
  sum = 0
  for line in f.read().splitlines():
    line_nums = []
    # n^2 solution but oh well
    for i in range(len(line)):
      for j in range(len(line)):
        if line[i:j + 1] in digits:
          line_nums.append(digits[line[i:j + 1]])
        elif line[i:j + 1].isnumeric():
          line_nums.append(int(line[i:j + 1]))
    sum += int(''.join([str(line_nums[0]), str(line_nums[-1])]))

  print(sum)
