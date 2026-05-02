import numpy as np


class MarkovChain:
    """
    A class that represents and solves a Markov Chain system

    This class reads Markov Chain data from a file, performs
    state transitions both forward and backward in time using matrix algebra,
    verifies the regularity of the system, and outputs the results to a formatted text file.

    Attributes
    ----------
    state : ndarray
        A 1D NumPy array representing the current population or probability
        distribution across the states of the system
    transition_matrix : ndarray
        A 2D square NumPy array where element T[i, j] represents the transition
        probability from state j to state i
    time_step : int
        The cumulative number of steps the system has moved from its initial
        state (can be positive or negative)
    required_steps : int
        The number of steps specified by the input data to move the system during
        the next calculation

    Methods
    -------
    read_chain_from_file(path)
        Reads a given data file and updates the attributes accordingly
    step()
        Updates the state vector by applying the transition matrix raised
        to the power of required_steps
    check_regularity()
        Returns a boolean that is True if the Markov Chain is regular, and False otherwise
    write_solution_to_file(path)
        Calls step() to calculate the final state, calls check_regularity()
        to determine whether the Markov Chain is regular, then writes the
        regularity, step direction, and final state values to a formatted text file.
    """

    def __init__(self):
        self.time_step = 0
        self.state = None
        self.transition_matrix = None
        self.required_steps = None

    def read_chain_from_file(self, path):
        """
        Reads a data file representing the transition matrix and initial state
        of the Markov Chain and updates the object attributes accordingly.

        Parameters
        ----------
        path : str
            The relative path to the data file.
        Methods
        -------
        np.array(object)
            Converts a list into a NumPy array.
        """
        # Open the file and read all lines
        with open(path, 'r') as f:
            lines = f.readlines()

        # Read the number of variables n from the first line
        n = int(lines[0])

        # Read the initial state vector from the second line
        self.state = np.array(lines[1].split())

        # Read the next n lines to build the transition matrix row by row
        self.transition_matrix = []
        for i in range(n):
            row = lines[i + 2].split()
            self.transition_matrix.append(row)
        self.transition_matrix = np.array(self.transition_matrix)

        # Read the required number of steps from the final line
        self.required_steps = int(lines[n + 2])

    def step(self):
        """
        Calculates the state of the system after n number of steps
        Updates state vector and increments number of steps taken

        Methods
        -------
        np.linalg.matrix_power(M, n)
            calculates the transition matrix M after n steps
        np.dot(V, P)
            transitions the state vector V according to matrix P
        """
        # Create n, the required number of steps to take
        n = self.required_steps

        # Calculate the n-th power of the transition matrix
        stepped_matrix = np.linalg.matrix_power(self.transition_matrix, n)

        # Update the state vector (no.dot using column vector convention)
        new_state = np.dot(stepped_matrix, self.state)
        self.state = new_state

        # Increment time_step with number of steps taken
        self.time_step += n

    def check_regularity(self):
        """
        Identifies whether the system is a regular Markov Chain or not

        Returns
        _______
        boolean
            True if Markov Chain is regular, False otherwise

        Methods
        _______
        np.linalg.matrix_power(transition_matrix, m)
            Used to perform matrix multiplication to calculate transition_matrix raised to power m
        np.all(condition)
            Used to verify if every element in transition matrix of power m is greater than 0

        """

        # set n
        n = self.transition_matrix.shape[0]

        # for an n x n matrix max m for T^m is given by:
        m_max = (n - 1) ** 2 + 1

        # calculate T^m (tm) for values of m up to m_max
        for m in range(1, m_max + 1):
            tm = np.linalg.matrix_power(self.transition_matrix, m)

            # if every element in matrix tm is > 0 return True
            if np.all(tm > 0):
                return True

        # if no matrix contains all positive values return False
        return False

    def write_solution_to_file(self, path):
        """
        Evaluates the Markov Chain, advances its state, and writes the results to a file.

        Arguments
        ---------
        path : str
            The file path where the solution output will be written.
            Creates or overwrites the file at the given path.
        """

        # Check whether the Markov Chain is regular before writing the result. Using Method 4
        is_regular = self.check_regularity()

        # Advance the current state by the required number of steps. Using Method 2
        self.step()

        # Open the output file in write mode.
        with open(path, 'w') as fp:
            # Write line 1: whether the Markov Chain is regular or not.
            if is_regular:
                fp.write('The Markov Chain is regular.\n')
            else:
                fp.write('The Markov Chain is not regular.\n')
            # Write line 2: describe whether the chain stepped forward, stepped backward, or did not step at all.
            if self.required_steps > 0:
                fp.write(f"The state has stepped forward by {self.required_steps} step(s).\n")
            elif self.required_steps < 0:
                fp.write(f"The state has stepped backward by {abs(self.required_steps)} step(s).\n")
            else:
                fp.write('No steps have been performed.\n')
            # Write the final state values.
            for final_state in self.state:
                fp.write(f"{final_state:.1f}\n")
