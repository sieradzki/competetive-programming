import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true')
args = parser.parse_args()

with open("intest" if args.t else "in") as f:
  lines = f.read().splitlines()
  sum = 0
  for i, line in enumerate(lines):
    ws = 0
    while ws < len(line):
      we = ws
      if line[ws].isnumeric():
        while line[ws:we + 1].isnumeric() and we <= len(line):
          we += 1

        chars_to_check = []
        if i != 0:
          chars_to_check.append(
            lines[i - 1][(ws - 1 if ws > 0 else ws):(we + 1 if we <= len(line) else we)])
        if i != len(lines) - 1:
          chars_to_check.append(
            lines[i + 1][(ws - 1 if ws > 0 else ws):(we + 1 if we <= len(line) else we)])
        if ws > 0:
          chars_to_check.append(line[ws - 1])
        if we <= len(line):
          chars_to_check.append((line[we]))

        chars_to_check = ''.join(chars_to_check)
        for char in chars_to_check:
          if char in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_', '=', '/']:
            sum += int(line[ws:we])
            break
        ws += we - ws
      else:
        ws += 1

  print(sum)
