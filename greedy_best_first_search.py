class Node:
    def __init__(self, value, cordinates, neighbors=None):
        self.value = value
        self.x = cordinates[0]
        self.y = cordinates[1]
        self.heuristic_value = -1
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors
        self.parent = None

    def has_neighbors(self):
        if len(self.neighbors) == 0:
            return False
        return True

    def number_of_neighbors(self):
        return len(self.neighbors)

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def extend_node(self):
        children = []
        for child in self.neighbors:
            children.append(child[0])
        return children

    def __gt__(self, other):
        if isinstance(other, Node):
            if self.heuristic_value > other.heuristic_value:
                return True
            if self.heuristic_value < other.heuristic_value:
                return False
            return self.value > other.value

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value
        return self.value == other

    def __str__(self):
        return self.value


class Graph:
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes

    def add_node(self, node):
        self.nodes.append(node)

    def find_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def add_edge(self, value1, value2, weight=1):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)

        if (node1 is not None) and (node2 is not None):
            node1.add_neighbor((node2, weight))
            node2.add_neighbor((node1, weight))
        else:
            print("Error: One or more nodes were not found")

    def number_of_nodes(self):
        return f"The graph has {len(self.nodes)} nodes"

    def are_connected(self, node_one, node_two):
        node_one = self.find_node(node_one)
        node_two = self.find_node(node_two)

        for neighboor in node_one.neighbors:
            if neighboor[0].value == node_two.value:
                return True
        return False

    def __str__(self):
        """
            Define the way the nodes of graph will be printed.
            Return
            ------
                str
        """
        graph = ""
        for node in self.nodes:
            graph += f"{node.__str__()}\n"
        return graph


class Greedy:


    def __init__(self, graph, start_position, target):
        self.graph = graph
        self.start = graph.find_node(start_position)
        self.target = graph.find_node(target)
        self.opened = []
        self.closed = []
        self.number_of_steps = 0

    def bangkok_distance(self, node1, node2):
        return abs(node1.x - node2.x) + abs(node1.y - node2.y)

    def insert_to_list(self, list_category, node):
        if list_category == "open":
            self.opened.append(node)
        else:
            self.closed.append(node)

    def remove_from_opened(self):
        self.opened.sort()
        node = self.opened.pop(0)
        # print(node)
        self.closed.append(node)
        return node

    def opened_is_empty(self):
        return len(self.opened) == 0

    def get_old_node(self, node_value):
        for node in self.opened:
            if node.value == node_value:
                return node
        return None

    def calculate_path(self, target_node):
        path = [target_node.value]
        node = target_node.parent
        while True:
            path.append(node.value)
            if node.parent is None:
                break
            node = node.parent
        path.reverse()
        return path

    def search(self):
        # Add the starting point to opened list
        self.opened.append(self.start)

        while True:
            self.number_of_steps += 1

            if self.opened_is_empty():
                print(f"No Solution Found after {self.number_of_steps} steps!!")
                break

            selected_node = self.remove_from_opened()
            if selected_node == self.target:
                path = self.calculate_path(selected_node)
                return path, self.number_of_steps

            # extend the node
            new_nodes = selected_node.extend_node()

            # add the extended nodes in the list opened
            if len(new_nodes) > 0:
                for new_node in new_nodes:

                    new_node.heuristic_value = self.bangkok_distance(new_node, self.target)
                    if new_node not in self.closed and new_node not in self.opened:
                        new_node.parent = selected_node
                        self.insert_to_list("open", new_node)
                    elif new_node in self.opened and new_node.parent != selected_node:
                        old_node = self.get_old_node(new_node.value)
                        if new_node.heuristic_value < old_node.heuristic_value:
                            new_node.parent = selected_node
                            self.insert_to_opened(new_node)


def main():
    # Create graph
    graph = Graph()
    # Add vertices
    graph.add_node(Node('S', (0, 0)))
    graph.add_node(Node('B', (0, 1)))
    graph.add_node(Node('C', (0, 3)))
    graph.add_node(Node('D', (1, 0)))
    graph.add_node(Node('E', (1, 1)))
    graph.add_node(Node('F', (1, 2)))
    graph.add_node(Node('G', (1, 3)))
    graph.add_node(Node('H', (2, 0)))
    graph.add_node(Node('I', (2, 3)))
    graph.add_node(Node('J', (3, 0)))
    graph.add_node(Node('K', (3, 1)))
    graph.add_node(Node('T', (3, 2)))
    graph.add_node(Node('M', (3, 3)))

    # Add edges
    graph.add_edge('S', 'B')
    graph.add_edge('S', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'G')
    graph.add_edge('D', 'E')
    graph.add_edge('D', 'H')
    graph.add_edge('E', 'F')
    graph.add_edge('F', 'G')
    graph.add_edge('G', 'I')
    graph.add_edge('H', 'J')
    graph.add_edge('I', 'M')
    graph.add_edge('J', 'K')
    graph.add_edge('K', 'T')
    graph.add_edge('T', 'M')

    # Execute the algorithm
    alg = Greedy(graph, "S", "T")
    path, path_length = alg.search()
    print(" -> ".join(path))
    print(f"Length of the path: {path_length}")


if __name__ == '__main__':
    main()

# S -> B -> E -> F -> G -> I -> M -> T
# Length of the path: 8
