from audioop import add
from collections import deque
from mimetypes import init
from platform import node
from pydoc import visiblename
import numpy as np
from search_problems import Node, GraphSearchProblem




def search_connection(finding_node,E,size,parents):
    add_to_queue = []
    nodes_expanded = 0
    for i in range(size):
        #find attatched node
        if ( E[i][0] == finding_node ):
            child = E[i][1]
            add_to_queue.append(child)
            parents[child] = finding_node
            # E = np.delete(E,i,0)
            # size -= 1
            nodes_expanded += 1
        elif ( E[i][1] == finding_node ):
            child = E[i][0]
            add_to_queue.append(child)
            parents[child] = finding_node
            # E = np.delete(E,i,0)
            # size -= 1
            nodes_expanded += 1
    return add_to_queue, size, nodes_expanded

def get_path(parents,init_state,goal_states):
    path = []
    current = goal_states[0]
    # while current != 8:
    for i in range(4):
        current = parents[current]
        print("meep")
        path.append(current)
    return path

def breadth_first_search(problem):
    """
    Implement a simple breadth-first search algorithm that takes instances of SimpleSearchProblem (or its derived
    classes) and provides a valid and optimal path from the initial state to the goal state. Useful for testing your
    bidirectional and A* search algorithms.

    :param problem: instance of SimpleSearchProblem
    :return: path: a list of states (ints) describing the path from problem.init_state to problem.goal_state[0]
             num_nodes_expanded: number of nodes expanded by your search
             max_frontier_size: maximum frontier size during search
    """
    
    max_frontier_size = 1
    num_nodes_expanded = 1
    path = []
    path.append(init_state)
    size = len(problem.E)
    visited = []
    copy_of_E = problem.E
    #queue for nodes to search
    to_search = []
    to_search.append(9)
    #dictionary of parents
    parents = {} # child:parent for all searches
    print(problem.E)
    #search for connection
    while to_search:
        print("to search:")
        print(to_search)
        checking = to_search.pop(0)
        print("checking:" + str(checking))
        if checking not in visited:
            print("not visited:" + str(checking))
            if checking == goal_states:
                print(parents)
                traced_path = get_path(parents,init_state,goal_states)
                print(traced_path)
                path.append(traced_path.reverse())
                return path, num_nodes_expanded, max_frontier_size
            else:
                visited.append(checking)
                add_to_queue,size,nodes_expanded = search_connection(checking,copy_of_E,size,parents)
                print("add to queue")
                print(add_to_queue)
                to_search += add_to_queue
                num_nodes_expanded += nodes_expanded
                current_frontier_size = len(to_search)
                if current_frontier_size > max_frontier_size:
                    max_frontier_size = current_frontier_size
        
    print("no solution found")
    return path, num_nodes_expanded, max_frontier_size


if __name__ == '__main__':
    # Simple example
    goal_states = [0]
    init_state = 9
    V = np.arange(0, 10)
    E = np.array([[0, 1],
                  [1, 2],
                  [2, 3],
                  [3, 4],
                  [4, 5],
                  [5, 6],
                  [6, 7],
                  [7, 8],
                  [8, 9],
                  [0, 6],
                  [1, 7],
                  [2, 5],
                  [9, 4]])
    problem = GraphSearchProblem(goal_states, init_state, V, E)
    path, num_nodes_expanded, max_frontier_size = breadth_first_search(problem)
    correct = problem.check_graph_solution(path)
    print("Solution is correct: {:}".format(correct))
    print(path)

    # Use stanford_large_network_facebook_combined.txt to make your own test instances
    E = np.loadtxt('C:/Users/User/Desktop/Python-Projects/ROB311-Lab1/rob311_winter_2022_project_01_handout/stanford_large_network_facebook_combined.txt', dtype=int)
    V = np.unique(E)
    goal_states = [349]
    init_state = 0
    # problem = GraphSearchProblem(goal_states, init_state, V, E)
    # path, num_nodes_expanded, max_frontier_size = breadth_first_search(problem)
    # correct = problem.check_graph_solution(path)
    # print("Solution is correct: {:}".format(correct))
    # print(path)