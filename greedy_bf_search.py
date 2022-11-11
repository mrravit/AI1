graphs = {
    'A': [('B', 20), ('C', 18), ('D', 25)],
    'B': [('C', 20), ('F', 20), ('J', 18)],
    'C': [('B', 20), ('L', 20), ('M', 23)],
    'D': [('E', 30), ('P', 25)],
    'F': [('G', 10), ('J', 25)],
    'H': [('I', 15)],
    'J': [('H', 10), ('K', 20)],
    'M': [('N', 19), ('O', 37), ('P', 16)],
    'N': [('Q', 30), ('X', 26)],
    'O': [('P', 22)],
    'P': [('X', 30)]
}

Heuristic_table = {
    'A': 79,
    'B': 70,
    'C': 50,
    'D': 53,
    'E': 80,
    'F': 75,
    'G': 60,
    'H': 50,
    'I': 70,
    'J': 40,
    'K': 20,
    'L': 12,
    'M': 20,
    'N': 15,
    'O': 10,
    'P': 30,
    'Q': 8,
    'X': 0
}


def path_h_cost(path):
    g_cost = 0
    for (node, cost) in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = Heuristic_table[last_node]
    return last_node, h_cost


def greedy_best_first_search(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_h_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)


def main():
    path = [('A', 0), ('B', 12), ('K', 22), ('J', 15)]
    cal = path_h_cost(path)
    print(cal)
    solution = greedy_best_first_search(graphs, 'A', 'X')
    print(f'Solution is {solution}')


if __name__ == '__main__':
    main()
