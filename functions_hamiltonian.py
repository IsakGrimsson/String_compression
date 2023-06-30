from Graph import *
import random
import math
import time
from datetime import datetime

def find_hamilton_path(n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alpha = alphabet[:n]

    # Create a graph
    my_graph = Graph()
    my_graph.populate(alpha)

    for i in range(10000):
        letter_list = list(alpha)
        test_string = ""
        while letter_list:
            index = random.randint(0, len(letter_list) - 1)
            test_string += letter_list.pop(index)
        hp = hamilton_path(my_graph.graph,test_string)
        if hp:
            print(hp)

def find_single_hamilton_path(n):
    n_letters = n
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(1, n_letters + 1):
        alpha = alphabet[:i]

        # Create a graph
        my_graph = Graph()
        my_graph.populate(alpha)
        hp = hamilton_path(my_graph.graph,alpha)

        # Progress bar
        time_stamp = time.time()
        date_time = datetime.fromtimestamp(time_stamp)

        print(alpha, '\t', "[", hp, "]", '\t', "The date and time is:", date_time)

def hamilton_path(g,alpha):
    factorial = math.factorial(len(alpha)-1)
    length = len(alpha)
    path=[]
    visited_rotations = []
    count = 0
    v = alpha
    while(count<length):
        # IF v is hasn't been visited, add it to the path, and then start another loop
        if g[v][0].rotation_id not in visited_rotations:
            visited_rotations.append(g[v][0].rotation_id)
            path.append(v)
            index = random.randint(0, length)
            for i in range(3):
                v = rotate(v)
            v = g[v][0].bbwt
        # ELSE find a new path
        else:
            bbwt = (g[v][0].bbwt)
            if g[bbwt][0].rotation_id not in visited_rotations:
                count = 0
                v = g[v][0].bbwt
            # otherwise keep rotating from v, until untread path found
            else:
                count += 1
                v = rotate(v)
        if len(visited_rotations) >= factorial:
            return path
    return False