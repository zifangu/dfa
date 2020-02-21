#!/usr/bin/env python3

"""
Ivan:
1. read in dfa.txt
2. put states, alphabets, start states, final states into separate lists
3. rules: create a dictionary of a 2-tuple (start, path) and end from dfa.txt
3.5 read in input.txt. start collecting paths
Noah:
4. create a function that take the 2-tuple, and return end state
Ivan:
5. the returned state is in a new 2-tuple (returned state, next char in file)
6. loop until the last char on the line is reached
Noah:
7. compare the returned result to the list of final states

"""



def open_file(filename):
    file = open(filename, "r")
    content = file.readlines()
    return content


def main():
    dfa = open_file("dfa.txt")
    start_states = []
    final_states = []
    rule_dictionary = {}
    # transition_rules = []
    counter = 0
    for line in dfa:
        print(line)

        if counter == 2:
            start_states.append(line[:-1])
        elif counter == 3:
            final_states.append(line[:-1])
        elif counter > 3:
            temp = line.split(",")
            rule_dictionary[(temp[0], temp[1])] = temp[2][:-1]
            # print(line[0])
        counter += 1

    print(start_states)
    print(final_states)
    print(rule_dictionary)







main()

