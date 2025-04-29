from decimal import Decimal, ROUND_HALF_UP, getcontext

fset = frozenset


class Graph:
    # Problem 1:
    #   Implement a code that checks if
    #   self.nodes and self.edges form a valid (finite) graph.
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def __repr__(self):
        '''returns string representation of graph for printing (was needed because of frozenset)'''
        return f"Graph(Nodes: {self.nodes}, Edges: {self.edges})"

    def is_valid(self):
        if len(self.edges) != len(set(self.edges)): # check whether duplicates in the graph
            print('there are duplicates in edges')
            return False
        for edge in self.edges:
            if len(edge) != 2: # each edge have to have two nodes - check whether this condition works
                print('each edge have to have'
                      'two nodes - invalid')
                return False
            for edge in self.edges: # check whether all the nodes are valid and exist in the graph
                for node in edge:
                    if node not in self.nodes:
                        print('edge contains nodes that are not in the graph')
                        return False

        return True

    def is_tree(self):
        #Problem 2:
        #   Implement a code that checks if
        #   this graph is a tree.

        if len(set(self.nodes)) != (len(set(self.edges)) + 1):
            print('there is not valid number of '
                  'nodes and edges - for each edge '
                  'there must be two vertices')
            return False
        else:
            self.adj_list = {node: [] for node in self.nodes}  # glossary of relatedness
            # like parent : children
            for u, v in self.edges:
                self.adj_list[u].append(v)
                self.adj_list[v].append(u)

        def depth(node, father):
            visited.add(node) # mark node as visited
            for neighbor in self.adj_list[node]:
                if not depth(neighbor, node):  # recursively call the function for this neighbour
                    return False  # if cycle inside is found - return False
                elif neighbor != parent:  # if the neighbor is visited and it is not parent - cycle is found
                    return False

            # start function from the first node
            if not depth(self.nodes[0], None):
                return False  # if cycle is found

            # chech whether all the nodes are visited - connection
            if len(visited) != len(self.nodes):
                return False

        return True
    def generate_subsets(self, node_list, index, current_subset, all_subsets): # function for generation subsets
        '''recursive function to generate all subsets of nodes  - going through all of them'''
        if index == len(node_list):  # base case: when all nodes are processed
            all_subsets.append(set(current_subset))  # store a copy of the subset
            return

        # exclude the current node
        self.generate_subsets(node_list, index + 1, current_subset, all_subsets)

        # include the current node
        current_subset.append(node_list[index])
        self.generate_subsets(node_list, index + 1, current_subset, all_subsets)

        # removing the last added node for the next iteration
        current_subset.pop()

    def subgraphs(self):
        '''Generate all subgraphs of the graph.'''
        all_subsets = []
        self.generate_subsets(list(self.nodes), 0, [], all_subsets) # - generate the subsests

        subgraphs = []
        for node_subset in all_subsets:
            edge_subset = {edge for edge in self.edges if all(node in node_subset for node in edge)} #going through subsets not by indexing
            # becausze of the frozenset
            subgraphs.append(Graph(node_subset, edge_subset)) # addind the found one

        return subgraphs

G = Graph(
    {'a', 'b', 'c', 'd'},
    {fset({'a','b'}), fset({'a','c'}), fset({'c','d'})}
)
print(G.nodes, G.edges, G.is_valid(), G.is_tree(), G.subgraphs())

'''in this task i still didn't has succeeded in making the characters absolutely accurate - 
but it's the best algorithm i've been able to do'''

def Pi(d):
    getcontext().prec = d + 15000 #change the precise calculating of number
    pi = Decimal(1)
    a = []
    sign = '-'
    for i in range(1, 10**5, 2):
        if sign == "+": # using the hint formula - calculating pi number
            a.append('1' + '/' + f'{(i + 2)}')
            pi += Decimal(1) / Decimal(i + 2)
            sign = '-' # chnging the sign
        else:
            pi -= Decimal(1) / Decimal(i + 2)
            a.append('-(1 / ' + f'{(i + 2)}')
            sign = "+"
    rez = Decimal(4) * pi
    answer = str(rez).replace('.', '')
    return answer[d-1] # return the d-th number

d = int(input('enter d-number '))
print(Pi(d))


def Palindromes(alphabet):
    queue = [""]  # start from an empty string
    while True:
        current = queue.pop(0)  # take first element

        # skip empty string - doesn't haved to be yeilded
        if current:
            yield current

        # add new palindromes, addind new elements
        for char in alphabet:
            queue.append(char + current + char)  # add symmetric strings
    #Problem 5:
    #   A palindrome is a string that looks the same forward and backward.
    #   Implement a generator that lists all palindromes using the given alphabet.
    #   See our main textbook 0.2 Strings and Languages

#this produces an infinite number of palindromes so i commented

'''for s in Palindromes({'a','b'}):
    print(s)'''