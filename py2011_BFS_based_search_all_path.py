# undirected graph
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
print(graph)


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
            print('result')
            print(result)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
        print('queue')
        print(queue)
    return result


rlt = bfs_paths(graph, 'A', 'F')
print('최종결과')
print(rlt)

print('')

'''

{'A': {'C', 'B'}, 'B': {'D', 'A', 'E'}, 'C': {'A', 'F'}, 'D': {'B'}, 'E': {'B', 'F'}, 'F': {'C', 'E'}}
queue
[('C', ['A', 'C']), ('B', ['A', 'B'])]
queue
[('B', ['A', 'B']), ('F', ['A', 'C', 'F'])]
queue
[('F', ['A', 'C', 'F']), ('D', ['A', 'B', 'D']), ('E', ['A', 'B', 'E'])]
result
[['A', 'C', 'F']]
queue
[('D', ['A', 'B', 'D']), ('E', ['A', 'B', 'E'])]
queue
[('E', ['A', 'B', 'E'])]
queue
[('F', ['A', 'B', 'E', 'F'])]
result
[['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
queue
[]
최종결과
[['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
'''
