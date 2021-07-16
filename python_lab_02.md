
## Zad. 1:
```python
for i in range(1, 10):
  print(i)
```
Wyświetla liczby od 1 do 9


## Zad. 2:
```python
for i in range(1, 10):
  print(i, end=' ')
```
Wyświetla liczby od 1 do 9 wyświetlając spacje zamiast znaku nowej linii na końcu


## Zad. 3:
```python
for i in range(1, 7):
  print(i * i, end=' ')
```


## Zad. 4:
Wypisanie sumy po wyjściu pętli/wypisanie przy każdej iteracji


## Zad. 5:
```python
total = 0
for number in range(0, 8, 2):
  total += number
```
```python
total = 12
number = 6
```


## Zad. 6:
```python
s = 'bioinfo'
for i in range(len(s)):
  print(s[i])
```
```python
❯ python .\zad.py
b
i
o
i
n
f
o
```


## Zad. 7:
```python
s2 = 'bioinfo'
```


## Zad. 8:
```python
age = 23
if age > 21:
  print('xxx')
elif age > 18:
  ...
```


## Zad. 9:
```python
name = input('Enter your name: ')                        # String
temp = float(input('Enter temperature in Celsius: '))    # Floating number

fahr_temp = 32 + 9/5 * temp
print(f'Temperature in Fahrenheit: {fahr_temp}')
```


## Zad. 10:
```python
seq = 'ATGCTGACT' 
position = 1

for char in seq:
  if char == 'T':
    print(position)
  position = position + 1
```


## Zad. 11:
```python
seq = input('Enter a DNA sequence: ')
mapping = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
print(''.join([mapping.get(i) for i in seq]))
```


## Zad. 12:
```python
>>> bool('A')
True
>>> bool('')
False
>>> bool(0)
False
>>> bool(0 or 2)
True
>>> bool(len('ATG') == 3)
True
>>> bool('T' in 'ATG')
True
>>> bool('C' not in 'ATG')
True
>>> bool(3 != 3)
False
>>> bool(('A' or '') and (2 or 0))
True
```


## Zad. 14:
Wypisuje kodony w alfabetycznej kolejności


## Zad. 15:
Nie


## Zad. 16:
Tak


## Zad. 17:
```python
lst1 = ['a', 'b', 'c']
lst2 = ['a', 'b', 'c']
```


## Zad. 18:
```python
lst1 = ['a', 'b', 'c']
lst2 = []
for letter in lst1:
    lst2.append(letter*2)
print(lst1)
print(lst2)
```


## Zad. 19:
```python
lst1 = ['a', 'b', 'c']
for index, _ in enumerate(lst1):
  lst1[index] *= 2
print(lst1)
```


## Zad. 20:
```python
human = [2269, 542, 54, 21]
mouse = [881, 179, 12, 11]

output = [x + y for x, y in zip(human, mouse)]
print(output)
```


## Zad. 21:
```python
3
5
1
6
2
4
```


## Zad. 22:
```python
print(list(range(4, 14, 3)))
print(list(range(10, 51, 10)))
print(list(range(33, 29, -1)))
```


## Zad. 23:
najmniejsza wartość\
największa wartość\
suma wszystkich elementów\
suma pierwszych trzech elementów\
liczba wystąpien liczby 15


## Zad. 24:
```python
lst = [10, 11, 12, 15, 13, 14, 15]
print(sum(lst) / len(lst))
```


## Zad. 25:
usuwa wystąpienie 15\
rozszerza listę o elementy innej listy\
dodaje 17 na pozycji 7\
odwraca


## Zad. 26:
rozdziela string po znakach białych\
rozdziela po 'I'\
usuwa znaki białe\
zamienia znaki białe na '-', i wszystkie litery na lowercase\
tworzy listę składającą się z wszystkich znaków w stringu


## Zad. 27:
```python
text = 'The Wellcome Trust Sanger Institute is a world leader in genome research.'
print(len(text.split()))
```


## Zad. 28:
```python
counts = [
  'A Ala 130856',
  'C Cys 21703',
  'D Asp 86498',
  'E Glu 106776',
  'F Phe 61151',
  'G Gly 112163',
  'H His 35961',
  'I Ile 94102',
  'K Lys 92360',
  'L Leu 152877',
  'M Met 38179',
  'N Asn 64319',
  'P Pro 74616',
  'Q Gln 62260',
  'R Arg 87607',
  'S Ser 104400',
  'T Thr 84597',
  'V Val 108836',
  'W Trp 17268',
  'Y Tyr 46259'
]

[print(x.split()[2]) for x in counts]
```


## Zad. 29:
```python
counts = [
    'A Ala 130856',
    'C Cys 21703',
    'D Asp 86498',
    'E Glu 106776',
    'F Phe 61151',
    'G Gly 112163',
    'H His 35961',
    'I Ile 94102',
    'K Lys 92360',
    'L Leu 152877',
    'M Met 38179',
    'N Asn 64319',
    'P Pro 74616',
    'Q Gln 62260',
    'R Arg 87607',
    'S Ser 104400',
    'T Thr 84597',
    'V Val 108836',
    'W Trp 17268',
    'Y Tyr 46259'
]

total = 1584224
for line in counts:
  aa, _, value = line.split()
  print(f'{aa} {int(value) * 100 / total:.2}')
```


## Zad. 30:
```python
True
True
True
False
True
False
True
```


## Zad. 31:
Iteracja po dwupoziomowej liście i wypisanie elementów


## Zad. 32:
```python
codons = [['TGA', 'TAA', 'TAG'], ['GAA', 'GAG'], ['TGG'], []]

for lst in codons:
  for codon in lst:
    for nucleotide in codon:
      print(nucleotide)
    print()

print()

for i in range(len(codons)):
  lst = codons[i]
  for j in range(len(lst)):
    codon = lst[j]
    for k in range(len(codon)):
      print(codon[k])
    print()
```


## Zad. 33:
```python
import statistics
numbers = [int(x) for x in input('Enter your numbers: ').split()]
print('Mean: ', statistics.mean(numbers))
```

## Zad. 34:
```python
buffer = input()
remaining_brackets = 0
for char in buffer:
  if char == '.':
    pass
  elif char == '(':
    remaining_brackets += 1
  elif char == ')':
    if remaining_brackets > 0:
      remaining_brackets -= 1
    else:
      raise RuntimeError('invalid bracket')
  else:
    raise RuntimeError('invalid character')

if remaining_brackets:
  raise RuntimeError('some brackets aren\'t closed')
else:
  print('correct structure')
```