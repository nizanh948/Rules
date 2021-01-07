#math modeling 
# network x 
import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np 
import random

# random_walks
def random_walks(G, matrix, iteration):
  '''
  # 000 no edge it only picks up once , # 010 it it produces an infinte loop 
  # only outer loop through three times so after the third time theres only one loop 
  # get the data 
  # a subset of letters
  ''' 
  matrix = [[0,0,1], [1,0,0], [0,0,0]] 
  x = random.randint(0, len(matrix)-1)
  for row  in range(iteration): # iteration 
      for col in range(len(matrix[0])):
          if matrix[x][col] == 1:
            add_nodes(G, x, col)
            add_edges(G, x, col)
             # print("x is ", x, "col is ", col)
            next = random.choice([x, col])
             # print("next is ", next)
            x = next 
              #print("row becomes", x)
              # the issue is that column dosent renew to 1? 
          #else:
          #if start 

def add_nodes(G, node1, node2):
  '''
  add nodes from the walk to a subset list to a graph to display 
  '''
  G.add_node(node1)
  G.add_node(node2)

    # check if the node exists in the graph twice
    # if not add the node seperate function 
    # add the edges between the nodes a sepreate fucntion # create that label
    # then you want to graph 
def add_edges(G, node1, node2):
  '''
  add edges between two created nodes and add there label 
  '''
  G.add_edge(node1, node2, label = str(node1)+' to '+str(node2))

             
# randomizing 2 function options
#option 1
'''
Where the graph has a subset of node amoutns 
as strings
def randomized_graph(G, nodes_set):
    count = 0 
    while count < len(G.nodes()+1):
      n_choice1 = random.choice(G.nodes())
      n_choice2 = random.choice(G.nodes())
      G.add_edge(n_choice1, n_choice2)
    return G 
'''

#option2
'''
Where a random amount of vertices and prob or edges are given, 
we create a random direction graph Nodes are integers

def random_graph(n, m):
  G = nx.gnm_random_graph(n,m, seed=None, directed=True)
  #  edge number = m
  #  node amount = n 
  return G 
'''
# main
def main():
  G =  nx.DiGraph() 
  matrix = [[0,0,0],[1,0,1],[0,1,0]]
  random_walks(G, matrix, 6)

  
  #print(random_walks(A))
  # choose a particula layout
  #pos = nx.circular_layout(G)
  nx.draw(G, with_labels=True)
  edge_labels=nx.draw_networkx_edge_labels(G,pos=nx.spring_layout(G))
  plt.show()
if __name__ == "__main__":
  main()