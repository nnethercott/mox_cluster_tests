#include "dealii_step40.hpp"

//pybind headers (not sure which of these are relevant)
#include <pybind11/pybind11.h>
#include <pybind11/attr.h>
#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/operators.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;


template<int dim>
void step40bind(pybind11::module &module){

  py::class_<Step40::LaplaceProblem<dim>>(module, "LaplaceProblem")
    .def(py::init<>()) //default constructor
    .def("setup_system", &Step40::LaplaceProblem<dim>::setup_system)
    .def("assemble_system", &Step40::LaplaceProblem<dim>::assemble_system)
    .def("solve", &Step40::LaplaceProblem<dim>::solve)
    .def("refine_grid", &Step40::LaplaceProblem<dim>::refine_grid)
    .def("setup_grid", &Step40::LaplaceProblem<dim>::setup_grid)
    .def("output_results", &Step40::LaplaceProblem<dim>::output_results);
    //.def("run", &Step40::LaplaceProblem<dim>::run);
}

PYBIND11_MODULE(LaplaceProblem, m) {
  step40bind<2>(m); //dimension 2 for fast sims
}

/*
int main(int argc, char *argv[])
{
  using namespace dealii;
  using namespace Step40;

  Utilities::MPI::MPI_InitFinalize mpi_initialization(argc, argv, 1);

  LaplaceProblem<2> laplace_problem_2d;

  //cycle 0
  GridGenerator::hyper_cube(laplace_problem_2d.triangulation);
  laplace_problem_2d.triangulation.refine_global(5);

  //setup
  laplace_problem_2d.setup_system();
}
*/
