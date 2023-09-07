lower = [chr(x) for x in range(97, 97 + 26)]
upper = [chr(x) for x in range(65, 65 + 26)]

alphabet = lower + upper
total = 0

with open("in") as f:
  for line in f.read().splitlines():
    comp1 = line[:len(line) // 2]
    comp2 = line[len(line) // 2:]

    dup = ''.join(set(comp1).intersection(comp2))
    index = alphabet.index(dup) + 1
    total += index

print(total)
