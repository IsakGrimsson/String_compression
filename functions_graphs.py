from collections import defaultdict
from functions_generic import *

class Vertex:
    def __init__(self, string):
        self.string = string
        self.rotation = "NA"
        self.rotation_id = "NA"
        self.bbwt = "NA"

    def add_rotation(self, new_vertex_string):
        self.rotation = new_vertex_string

    def add_rotation_id(self, id):
        self.rotation_id = id

    def add_bbwt(self, new_vertex_string):
        self.bbwt = new_vertex_string

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add a Vertex to the graph
    def add_vertex(self, vertex):
        self.graph[vertex.string].append(vertex)

    # function to return a Vertex
    def get_vertex(self, vertex_string):
        return self.graph.get(vertex_string)[0]

    def populate(self, string):
        stack = []  # Create a stack to keep track of vertices to process
        bbwt_stack = []
        stack.append(string)  # Add the initial string to the stack
        bbwt_stack.append(bbwt(string))  # Add the initial string to the stack
        rotation_id = 0

        while bbwt_stack:
            while stack:
                current_string = stack.pop()  # Get the topmost string from the stack
                if not self.graph[current_string]:
                    new_vertex = Vertex(current_string)
                    new_vertex.add_rotation(rotate(current_string))
                    new_vertex.add_rotation_id(rotation_id)
                    new_vertex.add_bbwt(bbwt(current_string))
                    self.add_vertex(new_vertex)

                if not self.graph[new_vertex.rotation]:
                    stack.append(new_vertex.rotation)  # Add the rotation to the stack

                if not self.graph[new_vertex.bbwt]:
                    bbwt_stack.append(new_vertex.bbwt)  # Add the bbwt to the stack
            new_string = bbwt_stack.pop()  # Get the topmost string from the stack
            stack.append(new_string)
            rotation_id += 1