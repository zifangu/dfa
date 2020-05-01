#!/usr/bin/env python3

"""
dfa.txt structure:
     Line 1: the states of the DFA (separated by commas, if there is more than one state)
 Line 2: the alphabet of the DFA (separated by commas, if there is more than one symbol)
 Line 3: the starting state of the DFA
 Line 4: the final/accept states of the DFA (separated by commas, if there is more than one accept state)
 Line 5 and onward: the transition rules, where each rule takes the form a,b,c (where being in state a and reading symbol b transitions to new state c)

Algorithm:
1. read in dfa.txt
2. Place states, alphabets, start states, final states into separate lists
3. rules: create a dictionary of a 2-tuple (start, path) and end from dfa.txt
3.5 read in input.txt. start collecting paths
4. create a function that take the 2-tuple, and return end state
5. the returned state is in a new 2-tuple (returned state, next char in file)
6. loop until the last char on the line is reached
7. compare the returned result to the list of final states
"""


def open_file(filename):
    file = open(filename, "r")
    content = file.readlines()
    file.close()
    return content


def return_states(string, dictionary, start_state):
    """
    :param string: input strings to be processed
    :param dictionary: 2-tuple is the key, the new state is the value
    :param start_state: initial state of the DFA
    :return: the last state after the entire string is processed
    """
    temp_state = start_state
    for i in string:
        # the new state is immediately processed as the new temp_state for the next character i
        temp_state = dictionary.get((temp_state, i))
        # print(temp_state)
    return temp_state


def print_result(file, result_list, final_states):
    counter = 1
    for i in result_list:
        if counter != len(result_list):
            if i in final_states:
                file.write("accept\n")
            else:
                file.write("reject\n")
        else:
            if i in final_states:
                file.write("accept")
            else:
                file.write("reject")
        counter += 1


def main():
    # opens the dfa.txt file and creates dictionary connecting the tuples and key
    dfa = open_file("dfa.txt")
    start_state = ""
    final_states = []
    rule_dictionary = {}
    # transition_rules = []
    counter = 0
    for line in dfa:
        line = line.strip()
        if counter == 2:
            start_state = line
            # print(start_state)
        elif counter == 3:
            final_states = line.split(",")

        elif counter > 3:
            # line = line.strip()
            temp = line.split(",")
            # print(temp)
            rule_dictionary[(temp[0], temp[1])] = temp[2]
            # print(line[0])
        counter += 1

    # print(start_states)
    # print("final:", final_states)
    # print(rule_dictionary)

    # read in different possibilities to see if accepted
    trans_states = open_file("input.txt")
    transition = []
    for line in trans_states:
        line = line.strip()
        transition.append(line)
    # print(transition)

    result_list = []
    for i in transition:
        result_list.append(return_states(i, rule_dictionary, start_state))

    # write the output file from result_list
    # print(result_list)
    output = open("output.txt", "w+")
    print_result(output, result_list, final_states)
    output.close()







main()

