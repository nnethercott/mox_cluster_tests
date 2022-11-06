#include <deal.II/base/utilities.h>
#include "../src/dealii_step40.hpp"
#include <iostream>
#include <chrono>
#include <deal.II/base/timer.h>

//not sure if these are covered in the dealii headers already
#include <map>
#include <string>

int main(int argc, char *argv[]){
  dealii::Utilities::MPI::MPI_InitFinalize mpi_initialization(argc, argv, 1);
  Step40::LaplaceProblem<3> l;

  //--------------------- simulation ----------------------------------
  int num_cycles = 25;
  auto t1 = std::chrono::high_resolution_clock::now();

  l.setup_grid();
  l.setup_system();
  l.assemble_system();
  l.solve();

  for(int i = 0; i<num_cycles; i++){
    l.refine_grid();
    l.setup_system();
    l.assemble_system();
    l.solve();
  }

  auto t2 = std::chrono::high_resolution_clock::now();
  auto diff = std::chrono::duration<double>(t2 - t1);
  double elapsed = 1000*diff.count();

  //what if we reduced and took the maximal runtime
  double average_process_runtime;
  MPI_Reduce(&elapsed, &average_process_runtime, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

  int rank, size;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &size);
  average_process_runtime/=size;

  //--------------------- output ---------------------------------
  if(rank == 0){
    std::cout<<average_process_runtime<<std::endl;
  }
}
