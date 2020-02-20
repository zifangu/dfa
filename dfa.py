#!/usr/bin/env python3

"""
1. read in dfa.txt
2. put states, alphabets, start states, final states into separate lists
3. rules: create a dictionary of a 2-tuple (start, path) and end from dfa.txt
3.5 read in input.txt. start collecting paths
4. create a function that take the 2-tuple, and return end state
5. the returned state is in a new 2-tuple (returned state, next char in file)
6. loop until the last char on the line is reached
7. compare the returned result to the list of final states

"""



def open_file(filename):
    file = open(filename, "r")
    content = file.read()
    return content
# simply testing


def main():
    dfa = open_file("dfa.txt")
    # states = []
    # alphabets = []
    # start_states = []
    # final_states = []
    # transition_rules = []










main()

