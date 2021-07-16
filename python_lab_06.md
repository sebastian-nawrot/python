## Zad. 1
```python
new_names = [f'Hs{x.upper()}' for x in names]
```


## Zad. 2
```python
>>> new_names
['HsTNRC6A', 'HsPRP', 'HsBAK1']
```


## Zad. 3
```python
>>> lst
[0, 2, 4, 6, 8]
```


## Zad. 4
```python
lst = [x*2 for x in string if x != 'N']
```


## Zad. 5
```python
len(t)
t[1]
list(t)
```


## Zad. 6
Jako klucz hash tabel


## Zad. 7
```python
>>> s | {'C', 'D'}
{'A', 'D', 'C', 'G'}
>>> s & {'C', 'D'}
{'C'}
>>> s - {'C', 'F'}
{'A', 'G'}
>>> len(s)
3
>>> s.issuperset({'G'})
True
>>> s.add('T')
>>> s
{'A', 'G', 'T', 'C'}
>>> s.add('G')
>>> s
{'A', 'G', 'T', 'C'}
>>> s.remove('A')
>>> s
{'G', 'T', 'C'}
```


## Zad. 8
```python
4
```


## Zad. 9
Wszystkie


## Zad. 10
```python
s[0]
s['A']
```


## Zad. 11
1\. Różnicę zbiorów\
2\. Sumę zbiorów\
3\. Część wspólną zbiorów\
4\. Różnicę symetryczną zbiorów


## Zad. 12
```python
>>> dna.issubset(nuc)
True
>>> dna <= nuc
True
>>> nuc < dna
False
>>> nuc <= nuc
True
>>> nuc.issuperset(dna)
True
>>> nuc >= dna
True
>>> nuc == dna
False
```


## Zad. 13
Wszystkie


## Zad. 14
```python
set(lst1) & set(lst2)
```


## Zad. 15
```python
rna_set.intersection(dna_dic)
rna_set.union(dna_dic)
```


## Zad. 16
```python
>>> set() == {}
False
>>> dict() == {}
True
```


## Zad. 17
A można jak najbardziej, jeszcze jak


## Zad. 18
```python
cancer1 = set(open('cancer1.txt').read().splitlines())
cancer2 = set(open('cancer2.txt').read().splitlines())
control = set(open('control.txt').read().splitlines())

open('cancer_common.txt', 'w').write('\n'.join(cancer1 & cancer2 - control))
```


## Zad. 19
```python
cancer1 = set(open('cancer1.txt').read().splitlines())
cancer2 = set(open('cancer2.txt').read().splitlines())
control = set(open('control.txt').read().splitlines())

open('cancer_common.txt', 'w').write('\n'.join(sorted(list(cancer1 & cancer2 - control))))
```


## Zad. 20
```python
from itertools import combinations

sequences = {}
with open('data/phages.fasta') as file:
  for line in file:
    if line.startswith('>'):
      id = line[1:].strip().split()[0]
      sequences[id] = ''
    else:
      sequences[id] += line.strip()

for id_x, id_y in list(combinations(sequences, 2)):
  sub_seqs_x = set([sequences[id_x][i:i+10] for i in range(0, len(sequences[id_x])-9)])
  sub_seqs_y = set([sequences[id_y][i:i+10] for i in range(0, len(sequences[id_y])-9)])
  jaccard_index = len(sub_seqs_x & sub_seqs_y) / len(sub_seqs_x | sub_seqs_y)
  print(f'{id_x}\t{id_y}\t{jaccard_index}')
```