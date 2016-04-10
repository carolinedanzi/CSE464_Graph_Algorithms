# CSE464_Graph_Algorithms

## How to Compile and Run
 - We are using Python 3, so you will need a Python 3 interpreter
 - Make sure your graph file (see proper format below) is in the same directory as the source code
 - Run Main.py in the interpreter, either by invoking the command `python Main.py` on the command line or by using IDLE.
 - Follow the directions in the menu.  It first asks you to enter the name of the graph file. Please type the entire filename (ex: graph.txt)

## Input Format for Graphs
### File Format
The textual representation of the graph you wish to analyze MUST be stored in a text (.txt) file.  It can have any file name you wish.

### Steps for Representing Graph
1. Number the nodes in your graph from 0 to the number of nodes in your graph minus one.
Example: If I have 4 nodes in my graph, I number them 0, 1, 2, 3.
2. Represent each edge in your graph in the following format: `source, destination, cost` where source and destination are integers representing the nodes in your graph, and cost is an integer.  Example: If node 2 is connected to node 3 with a cost of 5, then the edge is represented by 2,3,5 and 3,2,5 - if an edge is bidirectional, make sure you include both directions.
3. On the first line of the text file, and the first line only, write your graph in the following format:
`n $ edge list` where n is the total number of nodes in the graph and edge list is the list of the edges separated by semicolons (;)

Note:
 - Do not put a semicolon after the last edge in the list of edges
 - Spacing does not matter - you can put as many spaces between characters as long as you only use one line in the file
 
### Example
A connected graph with three nodes would be represented in the following way:
3 $ 0,1,52 ; 1,0,52 ; 1,2,33 ; 2,1,33 ; 0,2,45 ; 2,0,45
