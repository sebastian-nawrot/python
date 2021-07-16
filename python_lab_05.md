## Zad. 1
Winter is coming


## Zad. 2
```python
def gc_content(dna):
  c_count = dna.count('C') 
  g_count = dna.count('G') 
  content = (c_count + g_count) / len(dna)
  print(f"CG content is {content}")

dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT" 
gc_content(dna)
```


## Zad. 3
Pierwsza funkcja zwraca wypisuje wynik i zwraca None
Druga tylko zwraca wynik


## Zad. 4
```python
def gc_content(dna):
  c_count = dna.count('C') 
  g_count = dna.count('G') 
  content = (c_count + g_count) / len(dna)
  print(f"CG content is {content}")
  return content

dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT" 
print(gc_content(dna))
```


## Zad. 5
Tak, polimorfizm


## Zad. 6
```python
def hamming_distance(seq_x, seq_y):
  return sum(x != y for x, y in zip(seq_x, seq_y))

print(hamming_distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'))
```


## Zad. 7
```python
def hamming_distance(seq_x, seq_y):
  return sum(x != y for x, y in zip(seq_x.lower(), seq_y.lower()))

print(hamming_distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'))
```


## Zad. 8
7\. ```multiply(b=2, c=3)``` da 6


## Zad. 9
```python
88
99
```


## Zad. 10
```python
[3, 2, 1]
[1, 2, 3]
```


## Zad. 11
```python
[1, 3, 3]
[1, 3, 3]
```


## Zad. 12
int, len, list, min, max


## Zad. 13
Wypisują dokumentację funkcji print


## Zad. 14
```python
def hamming_distance(seq_x, seq_y):
  """ No jest wszystko w porządku, jest dobrze, dobrze robi, dobrze wszystko jest
  w porządku. Jest git pozdrawiam całą bioinformatykę, dobrych chłopaków i niech
  sie to trzyma. Dobry kod leci.

  Args:
    seq_x (str): First sequence
    seq_y (str): Second sequence

  Returns: The Hamming distance between two strings of equal length

  """
  return sum(x != y for x, y in zip(seq_x, seq_y))
```


## Zad. 15
```python
def complement(sequence):
  mapping = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
  return ''.join([mapping.get(i) for i in sequence])

print(complement('ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'))
```


## Zad. 16
```python
def complement(sequence):
  mapping = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
  return ''.join([mapping.get(i) for i in sequence])

def reverse_complement(sequence):
  return complement(sequence)[::-1]

print(complement('ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'))
print(reverse_complement('ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'))
```


## Zad. 17
```python
def complement(sequence):
  mapping = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
  return ''.join([mapping.get(i) for i in sequence])

def reverse_complement(sequence):
  return complement(sequence)[::-1]

lst = ['CTGACT', 'GCATAGT', 'TAGATTAT', 'CGATGTTTA']
[print(reverse_complement(each)) for each in lst]
```


## Zad. 18
Wyświetla 10 losowych liczb z zakresu 0-3


## Zad. 19
Wyświetla 10 losowych stringów z podanej listy


## Zad. 20
```python
import random

def mutate(sequence):
  lol = list(sequence)
  lol[random.randint(0, len(sequence) - 1)] = random.choice('ATCG')
  return ''.join(lol)

print(mutate('ATGCG'))
```