```python
import sys
from textwrap import wrap

def complement(sequence):
  mapping = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
  return ''.join([mapping.get(i) for i in sequence])

def reverse_complement(sequence):
  return complement(sequence)[::-1]


input_fasta   = 'Mycoplasma_hominis.fasta' if len(sys.argv) < 2 else sys.argv[1]
input_gtf     = 'Mycoplasma_hominis.gtf' if len(sys.argv) < 3 else sys.argv[2]
sequence_type = 'gene' if len(sys.argv) < 4 else sys.argv[3]


sequences = {}
with open(input_fasta) as file:
  for sequence in file.read().split('>'):
    if sequence:
      header, *content = sequence.splitlines()
      seqname = header[:header.find(' ')]
      sequences[seqname] = ''.join(content)


with open('genes.fasta', 'w') as out_file:
  with open('Mycoplasma_hominis.gtf') as file:
    for line in file:
      if line.startswith('#'):
        continue

      seqname, _, feature, start, end, _, strand, _, *attributes = line.split()
      if feature != sequence_type:
        continue

      assert attributes[0] == 'gene_id'
      gene_id = attributes[1][1:-2]
      out_file.write(f'>{seqname}|{feature}|{gene_id}|{start}:{end}|{strand}\n')

      gene_sequence = sequences[seqname][int(start):int(end)]
      if strand == '-':
        gene_sequence = reverse_complement(gene_sequence)

      for line in wrap(gene_sequence, 60):
        out_file.write(f'{line}\n')
```