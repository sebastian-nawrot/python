## Zad. 1:
Python 3.9.0


## Zad. 2:
```python
>>> 0 + 8
8
>>> 2 * 4
8
>>> 8 / 1
8.0
>>> 65 / 8
8.125
>>> 65 // 8
8
>>> 17 % 9
8
>>> 2 ** 4
16
>>> 64 ** 0.5
8.0
```


## Zad. 3:
```python
>>> type(17)
<class 'int'>
>>> type(1.618)
<class 'float'>
>>> type('1.618')
<class 'str'>
>>> type("1.618")
<class 'str'>
>>> type(1.6e-10)
<class 'float'>
>>> type(4E210)
<class 'float'>
>>> type(True)
<class 'bool'>
>>> type("bioinfo")
<class 'str'>
>>> type('3')
<class 'str'>
```


## Zad. 4:
```python
>>> 1 + 2 * 3
7
>>> (1 + 2) * 3
9
>>> 2 * 3.1
6.2
>>> 2.2 / 2.2
1.0
>>> (1 + 1) ** (5 - 2)
8
>>> 4 / 2 * 2
4.0
>>> 2 * 2 / 4
1.0
```


## Zad. 5:
```python
>>> a = 1
>>> b = 1 + 2
>>> print(b)
3
>>> c = a * a + b * b
>>> c
10
```


## Zad. 6:
```python
>>> a = 1
>>> a = 3.14
>>> a = 3 / 2
>>> type(a)
<class 'float'>
```


## Zad. 7:
```python
>>> a = 3
>>> b = a
>>> b = 4
>>> a
3
```


## Zad. 8:
```python
>>> a = 3
>>> b = a
>>> a = a + 2
>>> a
5
>>> b
3
```


## Zad. 9:
```python
>>> Gene = 2137
>>> exon = 2137
>>> 5utr = 2137
  File "<stdin>", line 1
    5utr = 2137
    ^
SyntaxError: invalid syntax
>>> utr5p = 2137
>>> gene name = 2137
  File "<stdin>", line 1
    gene name = 2137
        ^
SyntaxError: invalid syntax
>>> gene_name = 2137
>>> gene.name = 2137
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'gene' is not defined
>>> geneName = 2137
>>> UTR = 2137
```


## Zad. 10:
```python
>>> first = 'James'
>>> last = "Watson"
>>> name = first + ' ' + last
>>> name
'James Watson'
```


## Zad. 11:
```python
>>> len(name)
12
```


## Zad. 12:
```python
>>> '2' + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> '2' + '3'
'23'
>>> int('2') + 3
5
>>> '2' + str(3)
'23'
>>> float('2') + 3
5.0
>>> '2' * 3
'222'
>>> '2' * '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
```


## Zad. 13:
```python
>>> 'AT' * 7 + ' ATGC' * 7 + ' ' + 'CG' * 7
'ATATATATATATAT ATGC ATGC ATGC ATGC ATGC ATGC ATGC CGCGCGCGCGCGCG'
```


## Zad. 14:
```python
>>> s = '0123456789'
>>> s[0]
'0'
>>> s[1]
'1'
>>> s[9]
'9'
>>> s[10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> s[-1]
'9'
>>> s[-2]
'8'
```


## Zad. 15:
```python
>>> s[0:9]
'012345678'
>>> s[0:10]
'0123456789'
>>> s[:len(s)]
'0123456789'
>>> s[:]
'0123456789'
>>> s[:11]
'0123456789'
>>> s[-3:-1]
'78'
>>> s[-3:]
'789'
>>> s[1:10:2]
'13579'
>>> s[::2]
'02468'
>>> s[::-1]
'9876543210'
```


## Zad. 16:
```python
>>> s = 'Hello\tHolla\nGuten tag! Konnichi wa!'
>>> print(s)
Hello   Holla
Guten tag! Konnichi wa!
```

\n - znak nowej linii\
\t - tabulator


## Zad. 17:
```python
>>> s = s.upper()
>>> s
'BIOINFORMATICS'
```


## Zad. 18:
```python
>>> s = '  James Watson i Francis Crick odkryli strukturę DNA w 1953 roku.  '
>>> s.lstrip()
'James Watson i Francis Crick odkryli strukturę DNA w 1953 roku.  '
>>> s.rstrip()
'  James Watson i Francis Crick odkryli strukturę DNA w 1953 roku.'
>>> s.strip()
'James Watson i Francis Crick odkryli strukturę DNA w 1953 roku.'
>>> s.strip().rstrip('.')
'James Watson i Francis Crick odkryli strukturę DNA w 1953 roku'
>>> s.strip().rstrip(',')
'James Watson i Francis Crick odkryli strukturę DNA w 1953 roku.'
>>> s.find('Watson')
8
>>> s.find('Sherlock')
-1
>>> s.lower()
'  james watson i francis crick odkryli strukturę dna w 1953 roku.  '
>>> s.count('Watson')
1
>>> s.replace('o', '0')
'  James Wats0n i Francis Crick 0dkryli strukturę DNA w 1953 r0ku.  '
>>> s.strip().replace('roku.', 'roku!').upper()
'JAMES WATSON I FRANCIS CRICK ODKRYLI STRUKTURĘ DNA W 1953 ROKU!'
>>> s.strip().startswith('James')
True
>>> s.endswith('roku. ')
False
```


## Zad. 19:
```python
>>> sequence = ">MAnlFKLgaENIFLGrKW    "
>>> sequence[1:].strip().upper()
'MANLFKLGAENIFLGRKW'
```


## Zad. 20:
```python
>>> sequence = "AGCCGAGCCCGGCGGCCACGGCTGGCGATGAGGAGCGGCGGGTTAGAGCGCGAGC"
>>> sequence[:30].count('C')
11
```

## Zad. 21:
```python
>>> f'{"AT" * 7} {"ATGC " * 7}{"CG" * 7}'
```


## Zad. 22:
```python
# 01-22.py
seq = 'CGAGCGCGGCGCCCTTGAGCTGCACCGCGGCGCAGGTTTGCGAGCCGACTTGTCAGCCGG'
seqlen = len(seq)
print(seqlen)
```
```python
❯ python .\01-22.py
60
```
Wyświetla długość sekwencji


## Zad. 23:
```python
# 01-23.py
seq = 'CGAGCGCGGCGCCCTTGAGCTGCACCGCGGCGCAGGTTTGCGAGCCGACTTGTCAGCCGG'
seqlen = len(seq)
print(f'Sequence length: {seqlen} nt.')
```

## Zad. 24:
```python
# 01-24.py
seq = 'CGAGCGCGGCGCCCTTGAGCTGCACCGCGGCGCAGGTTTGCGAGCCGACTTGTCAGCCGG'
seqlen = len(seq)
gc_content = (seq.count('C') + seq.count('G')) * 100 / seqlen

print(f'Sequence length: {seqlen} nt.')
print(f'GC content: {gc_content}%')
```

## Zad. 25:
```python
# 01-25.py
chain_a = '''SSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKM
FCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVV
RRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFR
HSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILT
IITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKG
EPHHELPPGSTKRALPNNT'''

chain_splitted = chain_a.splitlines()
print(len(chain_splitted))

chain_merged = ''.join(chain_splitted)
print(chain_merged)
print(chain_merged[144:156])
print(chain_merged.find('NLRVEYLDDRN'))
print(chain_merged[chain_merged.find('SSS'):chain_merged.find('FCQ')])
```

## Zad. 26:
```python
# 01-26.py
dna = """GGGCTTGTGGCGCGAGCTTCTGAAACTAGGCGGCAGAGGCGGAGCCGCT
GTGGCACTGCTGCGCCTCTGCTGCGCCTCGGGTGTCTTTT
GCGGCGGTGGGTCGCCGCCGGGAGAAGCGTGAGGGGACAG
ATTTGTGACCGGCGCGGTTTTTGTCAGCTTACTCCGGCCA
AAAAAGAACTGCACCTCTGGAGCGG"""

dna_merged = ''.join(dna.splitlines())
rna = dna_merged.replace('T', 'U')
print(rna)

intron = rna[51:156]
print(intron

mrna = rna[:51] + rna[156:]
print(mrna)
```


