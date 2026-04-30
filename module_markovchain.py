import numpy as np

class MarkovChain:
    def __init__(self):
        self.time_step = 0
        self.state = None
        self.transition_matrix = None
        self.required_steps = None

    def read_chain_from_file(self,path):
        print("hello world")
        pass

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

        # Update the state vector
        self.state = np.dot(self.state, stepped_matrix)

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

        n = self.required_steps

        m_max = (n-1)**2 + 1

        for m in range(1, m_max + 1):
            tm = np.linalg.matrix_power(self.transition_matrix, m)

            if np.all(tm > 0):
                return True

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
        is_regular = self.check_regularity
        self.step()
        with open(path, 'w') as fp:
            if is_regular == 1:
                fp.write('The Markov Chain is regular\n')
            else:
                fp.write('The Markov Chain is not regular\n')
            if self.required_steps > 0:
                fp.write(f"The state has stepped forward by {self.required_steps} step(s)\n")
            elif self.required_steps < 0:
                fp.write(f"The state has stepped backward by {self.required_steps} step(s)\n")
            else:
                fp.write('No steps have been performed.')
            for final_state in self.state:
                fp.write(f"{final_state:.1f}\n")


