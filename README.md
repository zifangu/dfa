# dfa
Class project from Theory of Computation

The structure of dfa.txt will be as follows:

 Line 1: the states of the DFA (separated by commas, if there is more than one state) 
 
 Line 2: the alphabet of the DFA (separated by commas, if there is more than one symbol)
 
 Line 3: the starting state of the DFA
 
 Line 4: the final/accept states of the DFA (separated by commas, if there is more than one accept state)
 
 Line 5 and onward: the transition rules, where each rule takes the form a,b,c (where being in state a and reading symbol b transitions to new state c) 
 
 input.txt contains strings on each line that will run on the DFA.
 
 dfa.py will read in a text file called dfa.txt and construct a DFA. Then it reads in input.txt to determine whether each input strings can be accepted or not by the DFA. The result is reflected in output.txt as each line contains the result "acctpt" or "reject" for every line in input.txt.
 
 Files "input copy.txt" and "dfa copy.txt" are different test files for dfa.py. Both test cases produced consisent answers identical to the results from manually contructed DFAs (pencil and paper).
