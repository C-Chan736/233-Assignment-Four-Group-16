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
        ##
        ## test stephany
        pass

    def check_regularity(self):
        # 
        
        pass

    def write_solution_to_file(self, path):
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


