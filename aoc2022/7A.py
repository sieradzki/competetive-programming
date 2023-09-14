class Node():
  def __init__(self, name, parent, size=0):
    self.name = name
    self.parent = parent
    self.children = []
    self.size = size

  def print_tree(self, indent=0):
    print(' ' * indent + self.name + '\t' + str(self.size) +
          (' (dir)' if len(self.children) != 0 else ''))
    for child in self.children:
      child.print_tree(indent + 2)

  def is_child(self, name):
    for child in self.children:
      if child.name == name:
        return True
    return False

  def get_child_index(self, name):
    if not self.is_child(name):
      return -1
    for i, child in enumerate(self.children):
      if child.name == name:
        return i

  def calculate_size(self):
    for child in self.children:
      self.size += child.calculate_size()
    return self.size

  def get_dir_sizes(self):
    if len(self.children) == 0:
      return
    out = [self.size]
    for child in self.children:
      if len(child.children) > 0:
        out.extend(child.get_dir_sizes())
    return out


root = Node("/", None)
with open("in") as f:
  for line in f.read().splitlines():
    if "cd" in line.split(sep=' '):
      if "/" in line:
        cur = root
      elif ".." in line:
        if cur.parent == None:
          continue
        else:
          cur = cur.parent
      else:
        name = line.split(sep=' ')[-1]
        if not cur.is_child(name):
          cur.children.append(Node(name, cur))
          cur = cur.children[-1]
        else:
          cur = cur.children[cur.get_child_index(name)]

    elif line.startswith('dir'):
      name = line.split(sep=' ')[-1]
      if not cur.is_child(name):
        cur.children.append(Node(name, cur))

    elif line[0].isnumeric():
      size, name = line.split(sep=' ')
      if cur.is_child(name):
        continue
      else:
        cur.children.append(Node(name, cur, int(size)))

root.calculate_size()
# root.print_tree()
dir_sizes = root.get_dir_sizes()
# print(dir_sizes)

total = 0
for dir_size in dir_sizes:
  if dir_size < 100000:
    total += dir_size
print(total)
