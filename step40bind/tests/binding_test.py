import sys
sys.path.insert(1, '/root/lifex_mnt/examples/Nate/step40_dealii_example/build')
import LaplaceProblem as lp

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

l = lp.LaplaceProblem()

l.setup_grid()
l.setup_system()
l.assemble_system()
l.solve()

for i in range(num_cycles):
    l.refine_grid()
    l.setup_system()
    l.assemble_system()
    l.solve()
