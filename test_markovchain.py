#This is to test our file
import numpy as np
from module_markovchain import MarkovChain

## TESTING METHOD 1 ##

## TESTING METHOD 2 ##

## TESTING METHOD 3 ##

def test_method_3():
    markov_chain = MarkovChain()
    markov_chain.transition_matrix = np.array([
        [0.7, 0.2],
        [0.3, 0.8]
    ])
    result = markov_chain.check_regularity()
    assert (result == True)

## TESTING METHOD 4 ##

def test_method_4():
    chain = MarkovChain()

    chain.state = np.array([235.0, 365.0])
    chain.transition_matrix = np.array([
        [0.7, 0.2],
        [0.3, 0.8]
    ])
    chain.required_steps = 3

    chain.write_solution_to_file("test_output.txt")

    with open("test_output.txt", "r") as fp:
        print(fp.read())


test_method_4()


