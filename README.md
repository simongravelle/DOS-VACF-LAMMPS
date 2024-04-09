# DOS and VACF from LAMMPS dump

Python script for calculating vibrational density of states (DOS) from LAMMPS dump file.

An example of LAMMPS trajectory file can be optained by running the LAMMPS input file contained
within the LAMMPS-input/ folder. Run the lammps input file using:

```bash
    mpirun -np 8 lmp -in input.lammps -var rdm1 $RANDOM -var rdm2 $RANDOM -var rdm3 $RANDOM
```
where `lmp` is your LAMMPS executable.
