You are given an undirected graph consisting of n vertices. Initially there are no edges in the graph.
Also you are given q queries, each query either adds one undirected edge to the graph or removes
it. After each query you have to check if the resulting graph is bipartite (that is, you can paint all
vertices of the graph into two colors so that there is no edge connecting two vertices of the same
color).
Input
The first line contains two integers n and q (2 ≤ n, q ≤ 100 000).
Then q lines follow. The i-th line contains two numbers xi and yi (1 ≤ xi < yi ≤ n). These numbers
describe the i-th query: if there is an edge between vertices xi and yi

, then remove it, otherwise

add it.
Output
Print q lines. The i-th line must contain YES if the graph is bipartite after the i-th query, and NO
otherwise.
Example
Input
3 5
2 3
1 3
1 2
1 2
1 2

Output
YES
YES
NO
YES
NO
