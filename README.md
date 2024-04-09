# DOS and VACF from LAMMPS dump

Python script for calculating the vibrational density of states (DOS) from LAMMPS dump file.

## Theory

The density of state (DoS) has units of time and reads [1]

$$ S(\nu) = \dfrac{2}{k_\text{B} T} \sum_{j = 1}^N \sum_{k = 1}^3 s_j^k (\nu) $$

where $k_\text{B}$ is the Boltzmann constant, $T$ the temperature, $\nu$ the frequency, $N$ the
total number of atoms, and k = x, y, and z in the Cartesian coordinate. $s_j^k$ is the spectral density
of atom $j$ in the $k$ coordinate, has the units of distance$^2$ / time, and can be obtained by the Fourier Transform (FT) of $c_j^k$

$$ s_j^k (\nu) = \text{FT} (c_j^k) $$

where $c_j^k$ is the velocity autocorrelation of atom $j$ in the $k$ direction:

$$ c_j^k = \left< v_j^k (t) v_j^k (t + \tau) \right>. $$

The total velocity autocorrelation function $C(t)$ is the mass weighted sum of the atom velocity autocorrelation functions, it has the units of mass distance$^2$ / time, and reads

$$ C(t) = \sum_{j = 1}^N \sum_{k = 1}^3 m_j c_j^k (t). $$

$S(\nu)$ can be obtained from the Fourier transform of $C(t)$,

$$ S(\nu)$ = \dfrac{2}{k_B T} \text{FT} (C(t)).$$

## Example

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
