#!/bin/bash

lmp=/home/simon/Softwares/lammps-2Aug2023/src/lmp_mpi
mpirun -np 8 ${lmp} -in input.lammps -var rdm1 $RANDOM -var rdm2 $RANDOM -var rdm3 $RANDOM