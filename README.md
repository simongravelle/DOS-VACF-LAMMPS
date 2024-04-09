# DOS and VACF from LAMMPS dump

Python script for calculating vibrational density of states (DOS) from LAMMPS dump file.

An example of LAMMPS trajectory file can be optained by running the LAMMPS input file contained
within the LAMMPS-input/ folder. Run the lammps input file using:

```bash
    mpirun-np8${lmp} -ininput.lammps-varrdm1 $RANDOM -varrdm2 $RANDOM -varrdm3 $RANDOM
```
