#include <deal.II/base/utilities.h>
#include "../src/dealii_step40.hpp"
#include <iostream>
#include <deal.II/base/timer.h>

//not sure if these are covered in the dealii headers already
#include <map>
#include <string>

int main(int argc, char *argv[]){
  dealii::Utilities::MPI::MPI_InitFinalize mpi_initialization(argc, argv, 1);
  Step40::LaplaceProblem<2> l;
  Step40::TimeMap output_times = l.run();

  //should reformat the output print to csv-like
  for(auto it = output_times[0].begin(); it!=output_times[0].end();it++){
    std::cout<<it->first<<",";
  }
  std::cout<<std::endl;

  for(auto o: output_times){
    for(auto it = o.begin(); it!=o.end(); it++){
      std::cout<<it->second<<",";
    }
    std::cout<<std::endl;
  }
}
