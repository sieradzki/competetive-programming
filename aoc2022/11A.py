import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true')
args = parser.parse_args()

with open("intest" if args.t else "in") as f:
  index = 0
  monkeys = {}
  for line in f.read().splitlines():
    if line.startswith("Monkey"):
      index = int(line.split()[1][0])

    elif 'Starting' in line:
      line = line.replace(',', '')
      items = [int(word) for word in line.split() if word.isnumeric()]
      monkeys[index] = {}
      monkeys[index]['items'] = items
      monkeys[index]['insp_count'] = 0

    elif 'Operation' in line:
      op = line.split()[-2]
      val = line.split()[-1]

      monkeys[index]['op'] = op
      monkeys[index]['val'] = val

      match(op):
        case '*': pass
        case '+': pass

      match(val):
        case 'old': pass
        case other: pass

    elif 'Test' in line:
      div = int(line.split()[-1])
      monkeys[index]['test'] = div

    elif 'true' in line:
      monkey_index = int(line.split()[-1])
      monkeys[index]['true'] = monkey_index

    elif 'false' in line:
      monkey_index = int(line.split()[-1])
      monkeys[index]['false'] = monkey_index

  for round in range(20):
    for monkey, values in monkeys.items():
      for i, item in enumerate(values['items']):
        # operation
        val = item if values['val'] == 'old' else int(values['val'])
        match values['op']:
          case '*':
            item *= val
          case '+':
            item += val
        item = math.floor(item / 3)  # level drops after inspection

        test = item % values['test'] == 0

        if test:
          monkeys[values['true']]['items'].append(item)
        else:
          monkeys[values['false']]['items'].append(item)

        monkeys[monkey]['insp_count'] += 1

      monkeys[monkey]['items'].clear()

  monkey_business = 0
  insp_counts = []
  for key, values in monkeys.items():
    insp_counts.append(values['insp_count'])

  print(math.prod(sorted(insp_counts)[-2:]))
