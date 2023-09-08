lower = [chr(x) for x in range(97, 97 + 26)]
upper = [chr(x) for x in range(65, 65 + 26)]

alphabet = lower + upper
total = 0

with open("in") as f:
  lines = f.read().splitlines()

  while len(lines) >= 3:
    group = lines[:3]

    dup = ''.join(set(group[0]).intersection(group[1]).intersection(group[2]))

    total += alphabet.index(dup) + 1

    lines = lines[3:]

print(total)
