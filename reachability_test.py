import math
import time
from datetime import datetime
from functions_graphs import *

n_letters = 10
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(1, n_letters + 1):
    alpha = alphabet[:i]

    # Create a graph
    my_graph = Graph()
    my_graph.populate(alpha)
    graph_size = len(my_graph.graph)
    is_it_factorial = math.factorial(len(alpha)) == len(my_graph.graph)

    # Progress bar
    time_stamp = time.time()
    date_time = datetime.fromtimestamp(time_stamp)

    print(alpha, '\t', "[",  is_it_factorial, "]",'\t', "Timestamp:", date_time)