# DAA_CIA1


### Given Directed Graph

![image](https://user-images.githubusercontent.com/73640313/213088607-75d70d92-a81b-4fb9-9eb6-fb954c756a09.png)


### Prims Algorithm

* Step 1: Select a starting vertex  
* Step 2: Repeat Steps 3 and 4 until there are fringe vertices  
* Step 3: Select an edge 'e' connecting the tree vertex and fringe vertex that has minimum weight  
* Step 4: Add the selected edge and the vertex to the minimum spanning tree T  
[END OF LOOP]  
* Step 5: EXIT  

## Implementation

![image](https://user-images.githubusercontent.com/73640313/213093742-060cf5af-9739-49e1-ada7-12946e9a220d.png)

## Analysis
The time complexity of the above implementation of Prim's algorithm is O(n^2) and the space complexity is O(n^2)





### Kruskals Algorithm

* Step 1: Sort all edges in increasing order of their edge weights.
* Step 2: Pick the smallest edge.
* Step 3: Check if the new edge creates a cycle or loop in a spanning tree.
* Step 4: If it doesn’t form the cycle, then include that edge in MST. Otherwise, discard it.
* Step 5: Repeat from step 2 until it includes |V| - 1 edges in MST.

## Analysis

From my analysis
Kruskal's algorithm is a minimum spanning tree algorithm that works on undirected, weighted graphs. It cannot be used on directed, weighted graphs because it relies on the properties of undirected graphs, such as the fact that the edges do not have a direction and that the minimum spanning tree is unique. In directed weighted graph, there can be multiple spanning tree and also the edges have direction. Thus Kruskal's algorithm is not suitable for this case.
So I am thinking of convertying the directed graph to undirected graph and then applying kruskals algorithm. Else I have been thinking of penalizing or ignoring the negative weight.

The time complexity of the above implementation of Kruskal's algorithm is O(n^2 log n) and the space complexity is O(n).



### Djikstras Algorithm
Let the node at which we are starting be called the initial node. Let the distance of node Y be the distance from the initial node to Y. Dijkstra's algorithm will initially start with infinite distances and will try to improve them step by step.

* Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
* Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. During the run of the algorithm, the tentative distance of a node v is the length of the shortest path discovered so far between the node v and the starting node. Since initially no path is known to any other vertex than the source itself (which is a path of length zero), all other tentative distances are initially set to infinity. Set the initial node as current.[16]
* For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the one currently assigned to the neighbor and assign it the smaller one. For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbor B has length 2, then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.
* When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again (this is valid and optimal in connection with the behavior in step 6.: that the next nodes to visit will always be in the order of 'smallest distance from initial node first' so any visits after would have a greater distance).
* If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.
* Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new current node, and go back to step 3.


## Implementation

![image](https://user-images.githubusercontent.com/73640313/213097953-ab2ce751-c7e0-43f8-b9bb-4db9f66e5b2c.png)

## Analysis
The time complexity of the above code is O(n^2) and the space complexity is O(n)


## Justification for using Python Programming Language
Python is comfortable for me to use . I remember the syntax for python and I am not satisfied with myh work which I did now but I have utilzed my 2 hrs time to atleast make a analysis and I assure you that ill not stop working at this and I realized I have to focus more and concentrate. Loved the prtessure situation and realized a lot . 
This is my analysis mam

## Bellman Ford Algorithm 

Bellman Ford Algorithm is the best and efficient Algorithm to use for this scenario.

## Time Complexity 

Best Case Complexity	O(E)
Average Case Complexity	O(VE)
Worst Case Complexity	O(VE)

## Space complexity 
 the space complexity is O(V)

