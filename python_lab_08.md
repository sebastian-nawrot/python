## Zad. 1
Wypisują 2 i 3 elementowe kombinacje z podanej tablicy


## Zad. 2
```python
itertools.product(lst1, lst2, lst3)
```


## Zad. 3
Wypisuje bieżący katalog\
Tworzy folder o nazwie directory\
Uruchamia skrypt 08-03.py,\
Usuwa folder directory i plik 08-03.py


## Zad. 4
Wypisuje zawartość bieżącego katalogu\
Scala podane ciągi znaków jedną ścieżkę


## Zad. 5
Zlicza ilość nukleotydów/aminokwasów we wszystkich plikach .fasta w katalogu /human/genome


## Zad. 6
```python
>>> re.findall('dystrophin', text)
['dystrophin']
>>> re.findall('[Dd]ystrophin', text)
['dystrophin', 'Dystrophin']
>>> re.findall('\d', text)
['2', '3', '0', '0', '0', '0', '8', '7', '9', '1', '0', '7', '1', '4', '2', '0', '0', '4', '4', '2', '1', '0', '0', '1', '6', '1', '4']
>>> re.findall('\d\d', text)
['23', '00', '08', '79', '10', '14', '20', '44', '21', '00', '16', '14']
>>> re.findall('\d+', text)
['2300', '0', '08', '79', '107', '14', '200', '44', '2100', '16', '14']
>>> re.findall('\d+ kbp', text)
['2300 kbp', '200 kbp', '2100 kbp', '14 kbp']
>>> re.findall('\d+ k*bp', text)
['2300 kbp', '107 bp', '200 kbp', '2100 kbp', '14 kbp']
>>> re.findall('(\d+) k*bp', text)
['2300', '107', '200', '2100', '14']
>>> re.findall('[A-Z]+ gene', text)
['DMD gene']
>>> re.findall('The primary [^;]+', text)
['The primary transcript in muscle measures 2100 kbp and takes 16 hours\nto transcribe']
```


## Zad. 7
```python
>>> re.findall('intron\s+(\d+)', text)
['14', '44']
```


## Zad. 8
```python
>>> re.findall('(\d+.\d+)%', text)
['0.08']
```


## Zad. 9
Wyszukuje pierwsze wystąpienie wyrażenia regularnego w podanym ciągu znaków


## Zad. 10
Zwraca iterator wyszukujący wszystkie wystąpienia wyrażenia regularnego w podanym ciągu znaków


## Zad. 11
```re
[RKS][YFW][CTGH][VIL][FV]G[ADN]\w[VIL]\w\w\w\w[KR]
```


## Zad. 12
Wczytuje plik fasta z podanego urla


## Zad. 13
Wczytuje plik fasta z podanego urla i wypisuje pomijając nagłówki


## Zad. 14
```python
import urllib.request

with open('uniprot.txt', 'w') as file:
  for each in ['P68431', 'Q6ZQ08', 'O94687']:
    f = urllib.request.urlopen(f'http://www.uniprot.org/uniprot/{each}.fasta')
    file.write(f.read().decode('utf-8'))
```


## Zad. 15
Do przetwarzania parametrów wejściowych linii poleceń


## Zad. 16
```python
import argparse
import urllib.request

parser = argparse.ArgumentParser(description='Retrieve proteins from UniProt database')
parser.add_argument('-i', '--id', dest='uniprot', required=True,
                    nargs='+', help='Uniprot ID (e.g. P68431)')
parser.add_argument('-o', '--o', '--out', dest='output', default='uniprot.txt',
                    help='Output filename (default: %(default)s)')
args = parser.parse_args()

with open(args.output, 'w') as file:
  for each in args.uniprot:
    f = urllib.request.urlopen(f'http://www.uniprot.org/uniprot/{each}.fasta')
    file.write(f.read().decode('utf-8'))
```


## Zad. 17
```python
import argparse
import urllib.request

parser = argparse.ArgumentParser(description='Retrieve proteins from UniProt database')
parser.add_argument('-i', '--id', dest='uniprot', required=True,
                    nargs='+', help='Uniprot ID (e.g. P68431)')
parser.add_argument('-o', '--o', '--out', dest='output', default='uniprot.txt',
                    help='Output filename (default: %(default)s)')
parser.add_argument('--format', default='fasta')
args = parser.parse_args()

assert args.format in ('fasta', 'txt')

with open(args.output, 'w') as file:
  for each in args.uniprot:
    f = urllib.request.urlopen(f'http://www.uniprot.org/uniprot/{each}.{args.format}')
    file.write(f.read().decode('utf-8'))
```

## Zad. 18
```python
import re
from glob import glob

pattern = re.compile(r'[RKS][YFW][CTGH][VIL][FV]G[ADN]\w[VIL]\w\w\w\w[KR]')

for filepath in glob('data/GC/*.txt'):
  seq_name = filepath[filepath.rfind('\\')+1:-4]
  with open(filepath) as file:
    sequence = file.read().strip()
    for match in pattern.finditer(sequence):
      print(seq_name, match.group(0), match.span()[0], match.span()[1])
```