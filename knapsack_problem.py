import sys

w = [int(x) for x in sys.argv[1].split(',')]
s = [int(x) for x in sys.argv[2].split(',')]
b = int(sys.argv[3])

assert len(w) == len(s)
matrix = [[None for x in range(sum(w))] for y in range(len(w))] 

def dump_matrix():
  elements_width = max(len(str(sum(w))), len(str(len(w))))
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] != None:
        if len(str(matrix[i][j])) > elements_width:
          elements_width = len(str(matrix[i][j]))

  print(f'{" " * elements_width}  ', end='')
  for j in range(sum(w)):
    print(f'{j+1:>{elements_width}} ', end='')
  print()

  for i in range(len(matrix)):
    print(f'{i+1:>{elements_width}}', end='; ')
    for j in range(len(matrix[i])):
      if matrix[i][j] == None:
        print(' ' * elements_width, end=' ')
      else:
        print(f'{matrix[i][j]:>{elements_width}}', end=' ')
    print()


for i in range(len(w)):
  liczymy = True
  print(f'\niteracja {i+1}')

  wartosc = w[i]
  if i > 0 and matrix[i-1][wartosc-1] == None:
    matrix[i][wartosc-1] = s[i]
  elif i > 0 and matrix[i-1][wartosc-1] != None:
    if s[i] <= matrix[i-1][wartosc-1]:
      matrix[i][wartosc-1] = s[i]
    else:
      liczymy = True
      matrix[i][wartosc-1] = matrix[i-1][wartosc-1]
  elif i == 0:
    matrix[i][wartosc-1] = s[i]

  if i > 0:
    if liczymy:
      for j in range(len(matrix[i-1])):
        if matrix[i-1][j] != None:
          print(f'matrix[{i}][{wartosc+j}] = matrix[{i-1}][{j}] + {s[i]}'
                f' = {matrix[i-1][j]} + {s[i]} = {matrix[i-1][j] + s[i]}')

          assert matrix[i-1][j] != None

          if matrix[i-1][j] + s[i] <= b:
            if matrix[i-1][wartosc+j] != None and matrix[i-1][wartosc+j] < matrix[i-1][j] + s[i]:
              matrix[i][wartosc+j] = matrix[i-1][wartosc+j]
            else:
              matrix[i][wartosc+j] = matrix[i-1][j] + s[i]

    for j in range(len(matrix[i-1])):
      if matrix[i-1][j] != None:
        if matrix[i][j] == None:
          matrix[i][j] = matrix[i-1][j]

  dump_matrix()
  print()


# rozwiazanie
wiersze = []
koszty = []
wartosci = []
rozmiar = b
szukany = None

for i in reversed(range(len(matrix))):
  for j in reversed(range(len(matrix[i]))):
    if matrix[i][j] != None:
      if szukany != None and matrix[i][j] > szukany:
        continue

      if i > 0:
        if matrix[i][j] == matrix[i-1][j]:
          break
        elif matrix[i-1][j] != None and matrix[i-1][j] < matrix[i][j]:
          raise RuntimeError

      wiersze.append(i+1)
      koszty.append(s[i])
      wartosci.append(w[i])

      szukany = matrix[i][j] - s[i]
      rozmiar -= s[i]
      break


wiersze = list(reversed(wiersze))
koszty = list(reversed(koszty))
wartosci = list(reversed(wartosci))

print('wiersze:', wiersze)
print('koszty:', koszty, '=', sum(koszty))
print('wartosci:', wartosci, '=', sum(wartosci))