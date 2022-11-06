import sys
sys.path.insert(1, '/mnt/c/Users/naten/pyfex/nate/mox_cluster_tests/step40bind/build')
import LaplaceProblem as lp
import numpy as np

num_cycles = 5

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

l = lp.LaplaceProblem()

#--------------- simulation ---------------
t1 = MPI.Wtime()

l.setup_grid()
l.setup_system()
l.assemble_system()
l.solve()

for i in range(num_cycles):
    l.refine_grid()
    l.setup_system()
    l.assemble_system()
    l.solve()

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
