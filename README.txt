Implemented the value iteration algorithm for ﬁnding the optimal policy for each state of an MDP using Bellman’s equation. Program assumes an input ﬁle that contains a description of an MDP. Below is a sample input ﬁle:

s1 5 (a1 s1 0.509) (a1 s2 0.491) (a2 s1 0.31) (a2 s3 0.69) 
s2 10 (a1 s1 0.4) (a1 s2 0.3) (a1 s3 0.3) (a2 s2 0.5) (a2 s3 0.5) 
s3 -5 (a1 s1 0.3) (a1 s2 0.3) (a1 s3 0.4) (a2 s1 0.2) (a2 s2 0.8)

Each line in this ﬁle stores information for one state in the given MDP. 

For instance, the ﬁrst line stores information about state s1: the reward associated with s1 is 5, on action a1 we stay in s1 with probability 0.509 and move to s2 with probability 0.491, and on action a2 we stay in s1 with probability 0.31 and move to s3 with probability 0.69. The remaining lines of the ﬁle can be interpreted in a similar fashion.

After each of the ﬁrst 20 iterations of the value iteration algorithm, the program prints to stdout the J value and the optimal policy for each state of the given MDP. The output of the program looks like:

After iteration 1: (s1 a1 0.225) (s2 a3 5.456) (s3 a3 -2.435) 
After iteration 2: (s1 a2 1.224) (s2 a3 4.456) (s3 a1 -1.888) 
After iteration 3: (s1 a2 2.345) (s2 a3 4.252) (s3 a1 -1.098) ...

The ﬁrst line of the above output says that after iteration 1, the optimal action in s1 is a1 and J1(s1) = 0.225, the optimal action in s2 is a3 and J1(s2) = 5.456, and the optimal action in s3 is a3 and J1(s3) = −2.435. The remaining lines of output can be interpreted in a similar fashion.

The program takes exactly two arguments to be speciﬁed in the command line invocation : (1) an input file as described above, and (2) the discount factor (γ).
