#boilerplate
cmake_minimum_required(VERSION 3.8)
project(DEALII_VECTOR VERSION 1.0 LANGUAGES CXX)

# Force compiler to use C++17 standard.
set(CMAKE_CXX11_STANDARD_COMPILE_OPTION -std=c++17)
set(NATE_FLAGS "-Wall")
set(CMAKE_CXX_FLAGS "${NATE_FLAGS}")

################### deal.II ##################################
# Locate deal.II and initialize its variables.
find_package(deal.II 9.2.0 REQUIRED
  HINTS ${DEAL_II_DIR} $ENV{DEAL_II_DIR} $ENV{mkDealiiPrefix}
)
deal_ii_initialize_cached_variables()

################### pybind11 ##################################
include_directories(SYSTEM pybind11/include)
include_directories(SYSTEM $ENV{mkPythonInc})
add_subdirectory(/mnt/c/Users/naten/pyfex/pybind11 ../)
set(PYBIND11_LTO_CXX_FLAGS "OFF" CACHE INTERNAL "")
set(PYBIND11_LTO_LINKER_FLAGS "OFF" CACHE INTERNAL "")

##############################################################
ADD_EXECUTABLE(sim1 ./tests/test_parallel_effects.cpp)
DEAL_II_SETUP_TARGET(sim1)

ADD_EXECUTABLE(sim2 ./tests/test_cpp_vs_pybind.cpp)
DEAL_II_SETUP_TARGET(sim2)

pybind11_add_module(LaplaceProblem ./src/dealii_step40_bind.cpp)
DEAL_II_SETUP_TARGET(LaplaceProblem)
