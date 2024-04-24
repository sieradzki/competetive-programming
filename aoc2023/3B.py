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
      if line[ws] == '*':
        we = ws + 1
        # print(f"'{line[ws:we]}'")
        # exit()
        num_count = 0
        nums = []
        if i != 0:
          is_num = False
          for ci, char in enumerate(lines[i - 1][(ws - 1 if ws > 0 else ws):(we + 1 if we <= len(line) else we)]):
            if char.isnumeric() and is_num == False:
              is_num = True
              num_count += 1

              # Find the first digit of the number (move backwards)
              fd_i = ci + ws
              while fd_i > 0 and lines[i - 1][fd_i - 1].isnumeric():
                fd_i -= 1

              whole_num = ''
              for j in range(fd_i, len(lines[i - 1])):
                if lines[i - 1][j].isnumeric():
                  whole_num += lines[i - 1][j]
                else:
                  break

              # print(whole_num)
              nums.append(int(whole_num))
            else:
              is_num = False

        if i != len(lines) - 1:
          for ci, char in enumerate(lines[i + 1][(ws - 1 if ws > 0 else ws):(we + 1 if we <= len(line) else we)]):
            if char.isnumeric() and is_num == False:
              is_num = True
              num_count += 1

              # Find the first digit of the number (move backwards)
              fd_i = ci + ws
              while fd_i > 0 and lines[i + 1][fd_i - 1].isnumeric():
                fd_i -= 1

              whole_num = ''
              for j in range(fd_i, len(lines[i + 1])):
                if lines[i + 1][j].isnumeric():
                  whole_num += lines[i + 1][j]
                else:
                  break

              # print(whole_num)
              nums.append(int(whole_num))

            else:
              is_num = False

        if ws > 0:
          if line[ws - 1].isnumeric():
            num_count += 1

            fd_i = ws
            while fd_i > 0 and lines[i][fd_i - 1].isnumeric():
              fd_i -= 1

            whole_num = ''
            for j in range(fd_i, len(lines[i])):
              if lines[i][j].isnumeric():
                whole_num += lines[i][j]
              else:
                break

            print(whole_num)
            nums.append(int(whole_num))

        if ws <= len(line):
          if line[ws + 1].isnumeric():
            num_count += 1

            fd_i = ws
            while fd_i > 0 and lines[i][fd_i - 1].isnumeric():
              fd_i -= 1

            whole_num = ''
            for j in range(fd_i, len(lines[i])):
              if lines[i][j].isnumeric():
                whole_num += lines[i][j]
              else:
                break

            print(whole_num)
            nums.append(int(whole_num))

        if num_count == 2:
          sum += nums[0] * nums[1]

        ws += we - ws
      else:
        ws += 1

  print(sum)
