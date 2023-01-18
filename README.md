# DAA_CIA1


##Given Directed Graph

![image](https://user-images.githubusercontent.com/73640313/213088607-75d70d92-a81b-4fb9-9eb6-fb954c756a09.png)


##Prims Algorithm

*Step 1: Select a starting vertex  
*Step 2: Repeat Steps 3 and 4 until there are fringe vertices  
*Step 3: Select an edge 'e' connecting the tree vertex and fringe vertex that has minimum weight  
*Step 4: Add the selected edge and the vertex to the minimum spanning tree T  
[END OF LOOP]  
*Step 5: EXIT  

##Implementation

![image](https://user-images.githubusercontent.com/73640313/213093742-060cf5af-9739-49e1-ada7-12946e9a220d.png)

##Analysis



##Kruskals Algorithm

*Step 1: Sort all edges in increasing order of their edge weights.
*Step 2: Pick the smallest edge.
*Step 3: Check if the new edge creates a cycle or loop in a spanning tree.
*Step 4: If it doesn’t form the cycle, then include that edge in MST. Otherwise, discard it.
*Step 5: Repeat from step 2 until it includes |V| - 1 edges in MST.

##Analysis
From my analysis
Kruskal's algorithm is a minimum spanning tree algorithm that works on undirected, weighted graphs. It cannot be used on directed, weighted graphs because it relies on the properties of undirected graphs, such as the fact that the edges do not have a direction and that the minimum spanning tree is unique. In directed weighted graph, there can be multiple spanning tree and also the edges have direction. Thus Kruskal's algorithm is not suitable for this case.
So I am thinking of convertying the directed graph to undirected graph and then applying kruskals algorithm. Else I have been thinking of penalizing or ignoring the negative weight.
