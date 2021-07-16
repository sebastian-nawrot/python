## Zad. 1
```python
fh = open('sequences.fasta')
for line in fh:
  print(line)
fh.close()
```


## Zad. 2
```python
fh = open('sequences.fasta')
for line in fh:
  if line.lstrip().startswith('>'):
    print(line
fh.close()
```


## Zad. 3
```python
fh = open('sequences.fasta')
for line in fh:
  if line.lstrip().startswith('>'):
    print(line[1:].split()[0])
fh.close()
```


## Zad. 4
```python
fh = open('sequences.fasta')
for line in fh:
  if line.lstrip().startswith('>'):
    id, accession = line[1:].split()
    print(f'ID: {id} ACCESSION: {accession}')
fh.close()
```


## Zad. 5
```python
ids = []
fh = open('sequences.fasta')
for line in fh:
  if line.lstrip().startswith('>'):
    id, accession = line[1:].split()
    ids.append(id)
    print(f'ID: {id} ACCESSION: {accession}')
fh.close()
print(ids)
```


## Zad. 6
```python
plus = 0
fh = open('human.txt')
for line in fh:
  if not line.startswith('#'):
    if ' +' in line: 
      plus += 1
fh.close()
print(plus)
```


## Zad. 7
```python
plus = 0
fh = open('human.txt')
fh.readline()

for line in fh:
  if ' +' in line: 
    plus += 1
fh.close()
print(plus)
```


## Zad. 8
```python
plus = 0
total = 0

fh = open('human.txt')
fh.readline()

for line in fh:
  if ' +' in line: 
    plus += 1
  total += 1

fh.close()

print(f'Genes (+): {plus / total * 100}%')
print(f'Genes (+): {(total - plus) / total * 100}%')
```


## Zad. 9
```python
genes = []

fh = open('human.txt')
fh.readline()
for line in fh:
  columns = line.split()
  name = columns[0]
  start = int(columns[1])
  if start > 1000000:
    genes.append(name)
fh.close()

print(genes)
```


## Zad. 10
```python
genes = []

fh = open('human.txt')
fh.readline()
for line in fh:
  columns = line.split()
  name = columns[0]
  start = int(columns[1])
  end = int(columns[2])
  if start > 1000000:
    genes.append(name)
  print(f'{name}: {end - start}')

fh.close()

print(genes)
```


## Zad. 11
```python
genes = []
longest_name = None
longest_length = 0

fh = open('human.txt')
fh.readline()
for line in fh:
  columns = line.split()
  name = columns[0]
  start = int(columns[1])
  end = int(columns[2])
  length = end - start
  
  if start > 1000000:
    genes.append(name)
  print(f'{name}: {end - start}')

  if length > longest_length:
    longest_name = name
    longest_length = length

fh.close()

print(genes)
print(f'najdłuższy {longest_name}: {longest_length}')
```


## Zad. 12
```python
genes = []

fh = open('human.txt')
fh.readline()
for line in fh:
  columns = line.split()
  name = columns[0]
  start = int(columns[1])
  end = int(columns[2])
  length = end - start
  if start > 1000000:
    genes.append((length, name))
  print(f'{name}: {end - start}')

fh.close()

genes.sort(reverse=True)
[print(f'{x}: {y}') for x, y in genes[:3]]
```


## Zad. 13
Wczytuje całą zawartość pliku


## Zad. 14
```python
content = open('mobydick.txt').read().lower()
print(f'captain {content.count('captain')}')
print(f'whale {content.count('whale')}')
```


## Zad. 15
Otiwera plik i zapisuje do niego zawartość tablicy


## Zad. 16
SAMD11NOC2LKLHL17


## Zad. 17
```python
names = ['SAMD11', 'NOC2L', 'KLHL17']

oh = open('mygenes.txt', 'w')
for name in sorted(names):
    oh.write(f'{name}')
oh.close()
```


## Zad. 18
```python
names = ['OR4F5', 'OR4F29', 'OR4F16', 'SAMD11', 'NOC2L']
values = [918, 939, 939, 20654, 15106]

file = open('xd.txt', 'w')
for x, y in zip(names, values):
  file.write(f'{x} {y}\n')
```


## Zad. 19
```python
names = ['OR4F5', 'OR4F29', 'OR4F16', 'SAMD11', 'NOC2L']
values = [918, 939, 939, 20654, 15106]

file = open('xd.txt', 'w')
for x, y in reversed(sorted(zip(values, names))):
  file.write(f'{y} {x}\n')
```


## Zad. 20
```python
genes = []

fh = open('human.txt')
lol = open('human_length.txt', 'w')
fh.readline()
for line in fh:
  columns = line.split()
  name = columns[0]
  start = int(columns[1])
  end = int(columns[2])
  if start > 1000000:
    genes.append(name)
  print(f'{name}: {end - start}')
  lol.write(f'{name}: {end - start}\n')

fh.close()

print(genes)
```


## Zad. 21
```python
n = 0
with open('words_english.txt') as file:
  for line in file:
    word = line.strip()
    if word == word[::-1]:
      n += 1
print(f'Found {n} palindromes')
```


## Zad. 22
```python
n = 0
with open('words_english.txt') as file:
  with open('palindromes.txt', 'w') as output_file:
    for line in file:
      word = line.strip()
      if word == word[::-1]:
        output_file.write(word)
        n += 1
print(f'Found {n} palindromes')
```


## Zad. 23
```python
n = 0
with open('words_english.txt') as file:
  with open('palindromes.txt', 'w') as output_file:
    words = list(sorted(file.readlines(), key=len))    
    for word in words:
      word = word.strip()
      if word == word[::-1]:
        output_file.write(word + '\n')
        n += 1
print(f'Found {n} palindromes')
```


## Zad. 24
```python
from glob import glob

for filepath in glob('data/seq*.genbank.txt'):
  with open(filepath) as file:
    print(file.readline().strip().split()[1])
```


## Zad. 25
```python
from glob import glob

for filepath in glob('data/seq*.genbank.txt'):
  with open(filepath) as file:
    id = file.readline().strip().split()[1]
    
    sequence = ''
    switch = False
    for line in file:
      if line.startswith('ORIGIN'):
        for line in file:
          if line.startswith('//'):
            break
          sequence += ''.join(line.strip().split()[1:])
    
    print(f'{id} {(sequence.count("g") + sequence.count("c")) * 100 / len(sequence):.02f}')
```