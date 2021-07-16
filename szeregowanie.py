import networkx
import matplotlib.pyplot

n = 4
m = 3

p=[4, 2, 3, 3]
d=[4, 2, 4, 2]
r=[0, 1, 2, 0]


assert len(r) == len(p) == len(d)

print("# 1. L_max >= max{ r_j + p_j - d_j }")
l_max = max([r[j] + p[j] - d[j] for j in range(len(r))])

first_line = True
for j in range(len(r)):
  if first_line:
    print('L_max >= max {', f'{r[j]} + {p[j]} - {d[j]}', '} -> L_max >= max {',
      r[j] + p[j] - d[j], '} -> L_max >=', l_max)
    first_line = False
  else:
    print('             {', f'{r[j]} + {p[j]} - {d[j]}', '}                 {',
      r[j] + p[j] - d[j], '}')
print()


print("# 2. Przediały L_max = { r_i - d_j }")
all_values = []
for i in range(len(r)):
  r_values = []
  first_line = True
  for d_index in range(len(d)):
    current = r[i] - d[d_index]
    if first_line:
      print(f'r_{i} - d_j =', '{', f'{r[i]} - {d[d_index]}', '} = {', current, '}')
      first_line = False
    else:
      if current in r_values:
        print('            {', f'{r[i]} - {d[d_index]}', '}   {', current, '} # Można pominąć')
      else:
        print('            {', f'{r[i]} - {d[d_index]}', '}   {', current, '}')
    r_values.append(current)
  all_values.extend(r_values)
  print()

unique_values = sorted(set(all_values))
print('L_max € ', end='')
for i in range(len(unique_values)):
  if i == 0:
    print(f'(-inf, {unique_values[i]}>, ', end='')
  if i < len(unique_values) - 1:
    print(f'({unique_values[i]}, {unique_values[i+1]}>, ', end='')
  else:
    print(f'({unique_values[i]}, +inf)')

print(f'L_max € <{l_max}, +inf)')
print()


print("# 3. d_prim = d + L_max oraz e = { r } U { d_prim }")
d_prim = [each + l_max for each in d]
print(f'd^prim = {d} + {l_max} = {d_prim}')

e = sorted(set(r) | set(d_prim))
print(f'e = {r} + {d_prim} = {e}')
print()
  


print("# 4. Sieć przepływowa")

color_index = 0
colors = [
  #'#dfff00',
  '#ffbf00',
  '#ff7f50',
  '#de3163',
  #'#9fe2bf',
  '#40e0d0',
  '#6495ed',
  '#ccccff',
]

graph = networkx.DiGraph()
graph.add_node('s', layer=0)

left_side = {}
edge_labels = {}
for i in range(n):
  graph.add_node(f'T{i+1}', layer=1)
  graph.add_edge('s', f'T{i+1}')
  edge_labels[('s', f'T{i+1}')] = str(p[i])
  left_side[f'T{i+1}'] = p[i]



e_ranges = []
for i, current in enumerate(e[:-1]):
  e_ranges.append((current, e[i + 1]))
  graph.add_node(f'[{current}, {e[i+1]}]', layer=2)
#print(e_ranges)

networkx.set_edge_attributes(graph, 'black', 'color')



middle_side = {}
for i in range(n):
  for left, right in e_ranges:
    if r[i] <= left <= right <= d_prim[i]:
      if color_index < len(colors) - 1:
        graph.add_edge(f'T{i+1}', f'[{left}, {right}]', color=colors[color_index])
      else:
        graph.add_edge(f'T{i+1}', f'[{left}, {right}]', color='black')
      edge_labels[(f'T{i+1}', f'[{left}, {right}]')] = str(right - left)
      middle_side[f'T{i+1}', (str(left), str(right))] = right - left
  color_index += 1


right_side = {}
graph.add_node('t', layer=3)
for left, right in e_ranges:
  graph.add_edge(f'[{left}, {right}]', 't', color='black')
  edge_labels[(f'[{left}, {right}]', 't')] = str(m * (right - left))
  right_side[str(left), str(right)] = m * (right - left)



pos = networkx.multipartite_layout(graph, subset_key="layer")

colors = networkx.get_edge_attributes(graph, 'color').values()
networkx.draw(graph, pos=pos, with_labels=True, edge_color=colors,
  font_weight='bold', node_color='lightgreen')

networkx.draw_networkx_edge_labels(graph, pos=pos, label_pos=0.8,
  edge_labels=edge_labels, font_color='red')
matplotlib.pyplot.axis('off')



# 5.

rest_left = left_side
rest_middle = middle_side
rest_right = right_side


from collections import defaultdict

new_edges = {each: defaultdict(list) for each in graph.edges}

for left in left_side:
  for middle in middle_side:
    for right in right_side:
      if left == middle[0] and middle[1] == right:
        minimum = min(rest_left[left], rest_middle[middle], rest_right[right])
        if minimum == 0:
          continue

        rest_left[left] -= minimum
        rest_middle[middle] -= minimum
        rest_right[right] -= minimum

        if not new_edges['s', left]:
          edge_labels['s', left] += f', {minimum}'
        else:
          edge_labels['s', left] += f' + {minimum}'
        new_edges['s', left][left].append(minimum)

        if not new_edges[left, f'[{right[0]}, {right[1]}]']:
          edge_labels[left, f'[{right[0]}, {right[1]}]'] += f', {minimum}'
        else:
          edge_labels[left, f'[{right[0]}, {right[1]}]'] += f' + {minimum}'
        new_edges[left, f'[{right[0]}, {right[1]}]'][left].append(minimum)

        if not new_edges[f'[{right[0]}, {right[1]}]', 't']:
          edge_labels[f'[{right[0]}, {right[1]}]', 't'] += f', {minimum}'
        else:
          edge_labels[f'[{right[0]}, {right[1]}]', 't'] += f' + {minimum}'
        new_edges[f'[{right[0]}, {right[1]}]', 't'][left].append(minimum)

        print(f's{left}[{right[0]}, {right[1]}]t: DELTA = {minimum}')



for each, value in rest_left.items():
  if value:
    print(f"!!!! COFANIE Z {each}")


matplotlib.pyplot.clf() 

pos = networkx.multipartite_layout(graph, subset_key="layer")

colors = networkx.get_edge_attributes(graph, 'color').values()
networkx.draw(graph, pos=pos, with_labels=True, edge_color=colors,
  font_weight='bold', node_color='lightgreen')

networkx.draw_networkx_edge_labels(graph, pos=pos, label_pos=0.7,
  edge_labels=edge_labels, font_color='red')
matplotlib.pyplot.axis('off')


#matplotlib.pyplot.show()
matplotlib.pyplot.gcf().set_size_inches(14, 14)
matplotlib.pyplot.savefig(f'network.png')