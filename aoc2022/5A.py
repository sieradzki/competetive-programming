import math

# in_file = "intest"
in_file = "in"
n_stacks = 3 if in_file == "intest" else 9
stacks = [[] for _ in range(n_stacks)]

with open(in_file) as f:
  for line in f.read().splitlines():
    if '[' in line:
      for i, char in enumerate(line):
        if char.isalpha():
          # get index of crate
          index = math.ceil(i / 4) - 1
          # insert to the correct stack
          stacks[index].insert(0, char)

    elif "move" in line:
      instructions = []
      for word in line.split():
        if word.isnumeric():
          instructions.append(word)

      instructions = list(map(int, instructions))
      for _ in range(instructions[0]):
        x = stacks[instructions[1] - 1].pop()
        stacks[instructions[2] - 1].append(x)

out = ""
for stack in stacks:
  out += stack[-1]

print(out)
