Finally Fox Ciel arrived in front of her castle!
She has to type a password to enter her castle. An input device attached to her castle is a bit
unusual.
The input device is a 1 × n rectangle divided into n square panels. They are numbered 1 to n from
left to right. Each panel has a state either ON or OFF. Initially all panels are in the OFF state.
She can enter her castle if and only if the x1-th, x2-th, . . . , xk-th panels are in the ON state and
other panels are in the OFF state.
She is given an array a1, . . . , al

. In each move, she can perform the following operation: choose an
index i (1 ≤ i ≤ l), choose ai consecutive panels, and flip the states of those panels (i.e. ON →
OFF, OFF → ON).
Unfortunately she forgets how to type the password with only the above operations. Determine the
minimal number of operations required to enter her castle.
Input
The first line contains three integers n, k and l (1 ≤ n ≤ 10000, 1 ≤ k ≤ 10, 1 ≤ l ≤ 100), separated
by single spaces.
The second line contains k integers x1, . . . , xk (1 ≤ x1 < x2 < · · · < xk ≤ n), separated by single
spaces.
The third line contains l integers a1, . . . , al (1 ≤ ai ≤ n), separated by single spaces. It is possible
that some elements of the array a are equal.
Output
Print the minimal number of moves required to type the password. If it is impossible, print −1.
Examples
Input 1
10 8 2
1 2 3 5 6 7 8 9
3 5

Output 1
2

Input 2
3 2 1
1 2
3

Output 2
-1

Note
One possible way to type the password in the first example is the following: in the first move, choose
the 1st, 2nd and 3rd panels and flip them. In the second move, choose the 5th, 6th, 7th, 8th and
9th panels and flip them.
