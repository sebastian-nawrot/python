## Zad. 1
```python
>>> d = {}               # Pusty słownik
>>>
>>> d['A'] = 1           # przypisuje wartość 1 do klucza A
>>> d['B'] = 2           # przypisuje wartość 2 do klucza B
>>> d['A']               # wartość pod kluczem A
1
>>> len(d)               # ilość elementów w słowniku
2
>>> list(d.keys())       # tworzy listę z wszystkimi kluczami w słowniku
['A', 'B']
>>> list(d.values())     # tworzy listę z wszystkimi wartościami w słowniku
[1, 2]
>>> d['A'] = 3           # przypisuje wartość 3 do klucza A
>>> d['B'] += 3          # przypisuje 3 do wartości pod kluczem B
>>> 'A' in d             # sprawdza czy klucz 'A' znajduje się w słowniku
True
>>> 'A' not in d         # sprawdza czy klucz 'A' nie znajduje się w słowniku
False
```


## Zad. 2
```python
1
```


## Zad. 3
```python
[1, 2, 3]
```


## Zad. 4
```python
['A', 'B', 'C']
```


## Zad. 5
```python
[('A', 1), ('B', 2), ('C', 3)]
```


## Zad. 6
```python
KeyError: 'D'
```


## Zad. 7
```python
0
```


## Zad. 8
```python
4
```


## Zad. 9
Wypisuje klucze i ich wartości znajdujące się w słowniku


## Zad. 10
Wypisuje klucze i ich wartości znajdujące się w słowniku w posortowanej kolejności


## Zad. 11
```python
d = {
    'alpha': [1, 2, 3],
    'beta': 'bioinfo',
    'gamma': 4,
    'delta': {'key': 'val'}
}

print(d['alpha'])
d['alpha'].append(4)
print(d['alpha'][3])
print(d['beta'][0])
print(d['delta']['key'])
```


## Zad. 12
```python
l = [
  'gene1   54      3234',
  'gene2   6031    100321',
  'gene3   12381   142132'
]

d = {}
for line in l:
  key, val1, val2 = line.split()
  d[key] = [int(val1), int(val2)]
print(d)
```


## Zad. 13
```python
protein_weights = { 
  'A': 89.0932, 
  'C': 121.1582, 
  'D': 133.1027, 
  'E': 147.1293, 
  'F': 165.1891, 
  'G': 75.0666, 
  'H': 155.1546, 
  'I': 131.1729, 
  'K': 146.1876, 
  'L': 131.1729, 
  'M': 149.2113, 
  'N': 132.1179, 
  'O': 255.3134, 
  'P': 115.1305, 
  'Q': 146.1445, 
  'R': 174.201, 
  'S': 105.0926, 
  'T': 119.1192, 
  'U': 168.0532, 
  'V': 117.1463, 
  'W': 204.2252, 
  'Y': 181.1885 
}

pep = 'MRPSGTAGAALLALLAALCPASRALEEKKVCQGTSNKLTQLGTFEDHFLSLQRMFNNXCEVVLGNLEITYVQRNYDLSFLKTXIQEVAGYVL'

mm = 0
for aa in pep:
  mm += protein_weights.get(aa, 0)
print(mm)
```


## Zad. 14
```python
mapping = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}

dna = 'AGCCCGATGCTTA'
cdna = ''.join([mapping.get(i) for i in dna])
```


## Zad. 15
Zlicza wystąpienia każdego aminokwasu


## Zad. 16
```python
seq = 'MNNGGKAEKENTPSEANLQEEEVRTLFVSGLPLDIKPRELYLLFRPFKGYEGSLIKLTSKQPVGFVSFDSRSEAEAAKNALNGIRFDPEI'

d = {}
for char in seq:
  if char not in d:
    d[char] = 0
  d[char] += 1

for key, value in d.items():
  print(f'{key} {value / len(seq) * 100:.01f}')
```


## Zad. 17
```python
from collections import defaultdict

dna = 'AGCCCGATGCTTAAACGTAGATTTTCC'

counter = defaultdict(int)
for i in range(len(dna) - 1):
  counter[dna[i:i+2]] += 1

print(counter)
```


## Zad. 18
```python
d = {}
with open('ecoli.pep.fasta') as file:
  for each in filter(None, file.read().split('>')):
    header, *content = each.splitlines()
    d[header[:header.find(' ')]] = ''.join(content)
```


## Zad. 19
```python
protein_weights = { 
  'A': 89.0932, 
  'C': 121.1582, 
  'D': 133.1027, 
  'E': 147.1293, 
  'F': 165.1891, 
  'G': 75.0666, 
  'H': 155.1546, 
  'I': 131.1729, 
  'K': 146.1876, 
  'L': 131.1729, 
  'M': 149.2113, 
  'N': 132.1179, 
  'O': 255.3134, 
  'P': 115.1305, 
  'Q': 146.1445, 
  'R': 174.201, 
  'S': 105.0926, 
  'T': 119.1192, 
  'U': 168.0532, 
  'V': 117.1463, 
  'W': 204.2252, 
  'Y': 181.1885 
}

d = {}
with open('ecoli.pep.fasta') as file:
  with open('ecoli.mass.txt', 'w') as mass_file:
    for each in filter(None, file.read().split('>')):
      header, *content = each.splitlines()
      seq_name, seq = header[:header.find(' ')], ''.join(content)
      d[seq_name] = seq

      weights = map(lambda x: protein_weights.get(x, 0), seq)
      mass_file.write(f'{seq_name} {sum(weights):.01f}\n')
```

## Zad. 20
```python
from collections import Counter
from itertools import chain

with open('data/lotto_history.txt') as file:
  content = [x.strip().split()[2] for x in file.readlines()]
  numbers = [int(x) for x in chain.from_iterable(x.split(',') for x in content)]
  for number, occurrences in Counter(numbers).most_common(10):
    print(f'{number}: {occurrences}')
```