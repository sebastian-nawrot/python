import sys

class PartialDigest:
  def __init__(self, file):
    self.input_data = sorted([int(x) for x in file.read().split()])
    mapping = [self.input_data[-1] - self.input_data[-2]]
    self.result = self.find_map(self.input_data[-1], self.input_data, mapping)

  def find_map(self, left_size, fragments, mapping = []):
    if left_size in fragments:
      fragments.remove(left_size)
      if not fragments:
        return mapping

      for i in range(len(mapping)):
        if sum(mapping[i:]) not in fragments:
          return
        fragments.remove(sum(mapping[i:]))

      for each in fragments:
        new_fragments = fragments.copy()
        new_mapping = mapping + [each]

        result = self.find_map(left_size - mapping[-1], new_fragments, new_mapping)
        if result:
          return result

  def __iter__(self):
    self.n = 0
    return self

  def __next__(self):
    if self.n >= len(self.result):
      raise StopIteration
    current = self.result[self.n]
    self.n += 1
    return current

usage = '''Usage: python main.py nazwa_pliku
Program realizuje problem mapowania restrykcyjnego DNA metodą częściowego trawienia.
W folderze samples znajdują się 2 pliki z przykładowymi instancjami.
'''

if len(sys.argv) != 2:
  print(usage)
else:
  print(f'wynik: {[x for x in PartialDigest(open(sys.argv[1]))]}')