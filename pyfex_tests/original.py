import numpy as np

import sys,os
path_to_lib = '/mnt/c/Users/naten/pyfex/build/lib.linux-x86_64-3.9'
sys.path.insert(1, path_to_lib)

from CoupledReactionDiffusion import *

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#for command line arguments
import argparse
parser = argparse.ArgumentParser(description='A convenient way to modify sim params externally')
parser.add_argument('-r', "--refinement_reaction_diffusion", help="Specify mesh granularity", default=4)

args = parser.parse_args()

# dealii class construction
d = CoupledReactionDiffusion()

## Reaction model
d.model = "reaction_diffusion" # reaction_diffusion | diffusion

# Initialization
d.refinement_reaction_diffusion = int(args.refinement_reaction_diffusion)
d.alpha = 1.5
d.beta = 1

d.make_grid()

def run():
    # Setup system
    d.setup_system()

    # Assemble system
    d.assemble_system()

    # Solve system
    d.solve_system()

    # Set filename and output solution
    #d.filename = f'Solution_coupled_reaction_PACS{rank}' #comment this when running tests on cluster
    #d.output_results()


#-------------- simulation --------------

t1 = MPI.Wtime()
for i in range(int(args.iters)):
    run()
t2 = MPI.Wtime()

#--------------- output ---------------

diff = np.array(t2-t1)
average_process_runtime = np.zeros(1)

comm.Barrier()
comm.Reduce([diff, MPI.DOUBLE], [average_process_runtime, MPI.DOUBLE], op=MPI.SUM, root=0)

size = comm.Get_size()
average_process_runtime = average_process_runtime/size

if rank == 0:
    print(average_process_runtime)
