#This is to test our file
import numpy as np
from module_markovchain import MarkovChain
from numpy.testing import assert_allclose

## TESTING METHOD 1 ##

## TESTING METHOD 2 ##

def test_step_forward():
    # Test step function works with step of 1
    mc = MarkovChain()

    # Assign attributes
    mc.transition_matrix = np.array([[0.7, 0.2], [0.3, 0.8]])
    mc.state = np.array([200.0, 400.0])
    mc.required_steps = 1

    mc.step()

    expected = np.array([220.0, 380.0])
    assert_allclose(mc.state, expected)
    print("test_step_forward: PASSED")

def test_step_multistep():
    # Test step function works with step of 3
    mc = MarkovChain()

    # Assign attributes
    mc.transition_matrix = np.array([[0.7, 0.2], [0.3, 0.8]])
    mc.state = np.array([200.0, 400.0])
    mc.required_steps = 3

    mc.step()

    expected = np.array([235.0, 365.0]) # Array should be [235, 365] after 3 steps
    assert_allclose(mc.state, expected)
    print("test_step_multistep: PASSED")

def test_step_backward():
    # Test step function works with step of -1
    mc = MarkovChain()

    # Assign attributes
    mc.transition_matrix = np.array([[0.7, 0.2], [0.3, 0.8]])
    mc.state = np.array([220.0, 380.0])
    # Set time step to 1 for t = 1
    mc.time_step = 1

    mc.required_steps = -1
    mc.step()

    expected = np.array([200.0, 400.0])
    assert_allclose(mc.state, expected, atol = 1e-7) # atol = 1e-7 handles tiny decimal
    assert mc.time_step == 0
    print("test_step_backward: PASSED")

    print("testing method 2 ends here")

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


if __name__ == "__main__":
    test_step_forward()
    test_step_multistep()
    test_step_backward()
    print("tested 3 tests for method 2")
