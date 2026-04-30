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

def test_write_solution_to_file_forward():
    # Create a MarkovChain instance and assign initial attributes
    chain = MarkovChain()
    chain.state = np.array([200.0, 400.0])
    chain.transition_matrix = np.array([[0.7, 0.2], [0.3, 0.8]])
    chain.required_steps = 1

    # Write the solution to a file
    chain.write_solution_to_file("test_forward.txt")

    # Read the output file and store each line
    with open("test_forward.txt", "r") as fp:
        lines = fp.readlines()

    # Check regularity, step direction, and final state values
    assert lines[0] == "The Markov Chain is regular.\n"
    assert lines[1] == "The state has stepped forward by 1 step(s).\n"
    assert lines[2] == "220.0\n"
    assert lines[3] == "380.0\n"
    print("test_write_solution_to_file_forward: PASSED")


def test_write_solution_to_file_backward():
    # Create a MarkovChain instance and assign initial attributes
    # State is set to the result of 1 forward step so we can reverse it
    chain = MarkovChain()
    chain.state = np.array([220.0, 380.0])
    chain.transition_matrix = np.array([[0.7, 0.2], [0.3, 0.8]])
    chain.time_step = 1
    chain.required_steps = -1

    # Write the solution to a file
    chain.write_solution_to_file("test_backward.txt")

    # Read the output file and store each line
    with open("test_backward.txt", "r") as fp:
        lines = fp.readlines()

    # Check regularity, step direction, and final state values
    assert lines[0] == "The Markov Chain is regular.\n"
    assert lines[1] == "The state has stepped backward by 1 step(s).\n"
    assert lines[2] == "200.0\n"
    assert lines[3] == "400.0\n"
    print("test_write_solution_to_file_backward: PASSED")


def test_write_solution_to_file_no_steps():
    # Create a MarkovChain instance and assign initial attributes
    chain = MarkovChain()
    chain.state = np.array([200.0, 400.0])
    chain.transition_matrix = np.array([[0.7, 0.2], [0.3, 0.8]])
    chain.required_steps = 0

    # Write the solution to a file
    chain.write_solution_to_file("test_no_steps.txt")

    # Read the output file and store each line
    with open("test_no_steps.txt", "r") as fp:
        lines = fp.readlines()

    # Check regularity, no steps message, and state is unchanged
    assert lines[0] == "The Markov Chain is regular.\n"
    assert lines[1] == "No steps have been performed.\n"
    assert lines[2] == "200.0\n"
    assert lines[3] == "400.0\n"
    print("test_write_solution_to_file_no_steps: PASSED")


if __name__ == "__main__":
    #Test Method 1


    #Test Method 2
    test_step_forward()
    test_step_multistep()
    test_step_backward()
    #Test Method 3
    test_method_3()
    #Test Method 4
    test_write_solution_to_file_forward()
    test_write_solution_to_file_backward()
    test_write_solution_to_file_no_steps()