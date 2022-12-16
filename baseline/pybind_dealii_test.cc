/*
Pybind version of the previous function; just bind the function here
*/

#include <deal.II/base/index_set.h>
#include <iostream>
#include "mpi.h"

// pybind
#include <pybind11/pybind11.h>
namespace py = pybind11;

void example()
{
    using dealii::IndexSet;

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    IndexSet parallel_partitioning(size * 5);
    parallel_partitioning.add_range(rank * 5, (rank + 1) * 5);

    parallel_partitioning.print(std::cout);
}

PYBIND11_MODULE(Example, m)
{
    m.def("example", &example);
}