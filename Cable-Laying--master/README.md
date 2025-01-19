# Cable Laying Problem analysis.

- In this project, we had done the comparative analysis of two algorithms prims and  Kruskal's.  
- Both of them are minimum spanning trees.
- That means both the algorithm used to calculate the shortest path with minimum cost. 

### There are some applications of minimum spanning tree:
  - Network design
  - Approximation algorithm for NP-Hard
  - Cluster analysis.
  
### We picked up the network design application In which we consider that:
You have a business with several offices; you want to lease phone lines to connect them up with each other, and the phone company charges different amounts of money to connect different pairs of cities. You want a set of lines that connects all your offices with a minimum total cost. It should be a spanning tree, since if a network isn’t a tree you can always remove some edges and save money. 

**Upon this consideration, we take input from users:**
  - The number of cities.
  - How cities are connected with each other and the distance between them. 
  - Calculate the minimum cost using the adjacency matrix.

### We noticed that 
  - The advantage of Prim’s algorithm is its complexity, which is better than Kruskal’s algorithm. Therefore, Prim’s algorithm is helpful when dealing with dense graphs that have lots of edges.
  - However, Prim’s algorithm doesn’t allow us much control over the chosen edges when multiple edges with the same weight occur. The reason is that only the edges discovered so far are stored inside the queue, rather than all the edges like in Kruskal’s algorithm.

  <img src="https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-a748a2b3474677f82b24dfc5c38e6f02_l3.svg">

### Questions:
  - What is a minimum spanning tree?
  - The time complexity of both algorithms (worst and best)?
  - Is any other algorithm used to calculate MST? 
  - Implementation of both the algorithm.
