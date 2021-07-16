matrix = [
  [0, None, None, None, 1, None],
  [4, 0, None, 1, None, 5],
  [None, 6, 0, None, 3, None],
  [None, 5, None, 0, 2, None],
  [None, 2, None, None, 0, 1],
  [3, None, 2, None, None, 0],
]


for row in matrix:
  assert len(row) == len(matrix)

vertices = []
for i in range(len(matrix)):
  vertices.append(str(i + 1))
print(f'vertices: {vertices}')


def dump_matrix():
  elements_width = len(max(vertices, key=len))
  for i in range(len(vertices)):
    for j in range(len(vertices)):
      if matrix[i][j] != None:
        if len(str(matrix[i][j])) > elements_width:
          elements_width = len(str(matrix[i][j]))

  print(f'{" " * elements_width}  ', end='')
  for j in range(len(vertices)):
    print(f'{vertices[j]:>{elements_width}} ', end='')
  print()

  for i in range(len(vertices)):
    print(f'{vertices[i]:>{elements_width}}', end='; ')
    for j in range(len(vertices)):
      if matrix[i][j] == None:
        print(' ' * elements_width, end=' ')
      else:
        print(f'{matrix[i][j]:>{elements_width}}', end=' ')
    print()



dump_matrix()

for i in range(len(vertices)):
  print(f'\niteracja {i+1}')

  for j in range(0, len(vertices)):
    for k in range(0, len(vertices)):
      if j == i or k == i:
        continue

      if j != k:
        if matrix[j][i] != None and matrix[i][k] != None:
          if matrix[j][k] == None or matrix[j][k] > matrix[j][i] + matrix[i][k]:
            matrix[j][k] = matrix[j][i] + matrix[i][k]

  dump_matrix()