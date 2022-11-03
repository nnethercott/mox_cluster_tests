import sys
sys.path.insert(1, '/root/lifex_mnt/examples/Nate/step40_dealii_example/build')
import LaplaceProblem as lp

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()


l = lp.LaplaceProblem()

'''
without binding the grid generator function in the run method we can't manually execute this;
some solutions:
    - just define a run_setup()
    - bind the dealii function
'''
l.run()
