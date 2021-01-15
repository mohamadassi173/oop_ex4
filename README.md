# ***About the project***

The project represents an implementation of directed weighted graph with different methods and algorithms in python language.
an implementation of Dijkstra's algorithm  to find the shortest path between two vertices and BFS algorithm for to find Strongly Connected Components
and print the graph using plotlibrary.


***save:*** save the graph to the given file name using json method.

***load:*** load a graph from the given file name to to a graph.

***getGraph:*** returns the graph on which we operate the algorithms

***ConnectedComponents:*** Finds the Strongly Connected Components(SCC) of the graph.

***shortestPath:*** return the distnace from source node to dest node and the list that represents the path.


# ***Algorithms:*** 

Dijkstra's algorithm (or Dijkstra's Shortest Path First algorithm, SPF algorithm) is an algorithm for finding the shortest paths between nodes in a graph.
Analysis for dijkstra's: a.Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
b.Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. Set the initial node as current.
c.For the current node, consider all of its unvisited neighbours and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one
d.When we are done considering all of the unvisited neighbours of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again.
e.If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.
f.Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step e.

Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. 
It starts at the tree root (or some arbitrary node of a graph and explores all of the neighbor nodes at the present
 depth prior to moving on to the nodes at the next depth level.

 ![4999443](https://user-images.githubusercontent.com/58177069/104652022-2850e880-56c1-11eb-835b-931ba0e01fb2.png)


<img width="960" alt="graph_a5 (1)" src="https://user-images.githubusercontent.com/58177069/104652326-9e554f80-56c1-11eb-83e7-525d46f254d3.PNG">
