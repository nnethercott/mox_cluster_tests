# Imports
#from pyfex_init import *

import numpy as np
#import scipy.io
#import pickle


import sys,os
sys.path.insert(1, '/mnt/c/Users/naten/pyfex/build/lib.linux-x86_64-3.9')
#from RB_library import *
from arrayBind import *
from CoupledReactionDiffusion import *

#i think we can make this work by just initing MPI externally
'''param_file = 'none.prm'
output_path = 'results/'
e = pyfex_init(param_file,False,2,output_path)'''

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#for command line arguments
import argparse
parser = argparse.ArgumentParser(description='A convenient way to modify sim params externally')
parser.add_argument('-r', "--refinement_reaction_diffusion", help="Specify mesh granularity", default=4)

args = parser.parse_args()


def run():
    # dealii class construction
    d = CoupledReactionDiffusion()

    ## Reaction model
    d.model = "reaction_diffusion" # reaction_diffusion | diffusion

    # Initialization
    #increasing this value increases dofs, issues might incur with 6+
    d.refinement_reaction_diffusion = int(args.refinement_reaction_diffusion)
    d.make_grid()

    # Setup system
    d.setup_system()

    # Set parameters
    d.alpha = 1.5
    d.beta = 1
    #new (added by Nate according to same syntax as dealii tutorial)

    # Assemble system
    d.assemble_system()

    # Solve system
    d.solve_system()

    # Set filename and output solution
    d.filename = f'Solution_coupled_reaction_PACS{rank}' #comment this when running tests on cluster
    #d.output_results()


run()
