matrix = [
  [0, 5, None, 2, None, None],
  [None, 0, 3, None, None, 1],
  [8, None, 0, None, 2, None],
  [None, None, 5, 0, None, 2],
  [None, 6, None, 3, 0, None],
  [9, None, None, None, 1, 0],
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
            print('# add', vertices[j], vertices[k], 'replace', matrix[j][k], 'with', matrix[j][i] + matrix[i][k])
            matrix[j][k] = matrix[j][i] + matrix[i][k]

  dump_matrix()