# undirected graph
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
print(graph)


def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        print(n)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
            print(queue)
    return visited


rlt = bfs(graph, "A")
print(rlt)
print("")

''''
{'A': {'C', 'B'}, 'B': {'D', 'E', 'A'}, 'C': {'F', 'A'}, 'D': {'B'}, 'E': {'F', 'B'}, 'F': {'C', 'E'}}
A
['C', 'B']
C
['B', 'F']
B
['F', 'D', 'E']
F
['D', 'E', 'E']
D
['E', 'E']
E
['E']
E
['A', 'C', 'B', 'F', 'D', 'E']

'''
