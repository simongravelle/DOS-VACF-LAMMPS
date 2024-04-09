# DOS and VACF from LAMMPS dump

## Theory

The density of state (DoS) has units of time and reads [1]

$$ S(\nu) = \dfrac{2}{k_\text{B} T} \sum_{j = 1}^N \sum_{k = 1}^3 s_j^k (\nu) $$

where 

Python script for calculating the vibrational density of states (DOS) from LAMMPS dump file.

An example of LAMMPS trajectory file can be obtained by running the LAMMPS input file contained
within the LAMMPS-input/ folder. Run the LAMMPS input file using:

```bash
    mpirun -np 8 lmp -in input.lammps
```
where `lmp` is your LAMMPS executable.

## VACS and DOS

An example of calculation can be found in the Notebook [calculateDOS](calculateDOS.ipynb).

![illustration](figures/vacf-dark.png#gh-dark-mode-only)

![illustration](figures/vacf-light.png#gh-light-mode-only)

![illustration](figures/dos-dark.png#gh-dark-mode-only)

![illustration](figures/dos-light.png#gh-light-mode-only)

## Sources

Inspired by [dump2VDOS](https://zenodo.org/records/10573320), please cite them if you use this script.

## Reference

[1] Lin, Blanco, and Goddard, J. Chem. Phys., 2003, 119, 22 
