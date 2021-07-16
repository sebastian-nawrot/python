graph = [
  (1, 2, 4),
  (2, 3, 4),
  (2, 4, 2),
  (3, 4, 4),
  (4, 5, 4),
  (5, 1, 1),
  (5, 2, 1),
  (5, 3, 1),
]


graph = [(str(x), str(y), w) for x, y, w in graph]
edges = {(x, y): w for x, y, w in graph}

vertices = set()
for x, y, _ in graph:
  vertices.update([x, y])
vertices = list(sorted(vertices))
print(f'vertices: {vertices}')


matrix = [[None for x in range(len(vertices))] for y in range(len(vertices))] 
for i in range(len(vertices)):
  for j in range(len(vertices)):
    if i == j:
      matrix[i][j] = 0
    else:
      if (vertices[i], vertices[j]) in edges.keys():
        matrix[i][j] = edges[(vertices[i], vertices[j])]


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