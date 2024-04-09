import os, sys, shutil
import numpy as np

import numpy as np
from pint import UnitRegistry
ureg = UnitRegistry()

def create_parameter_lammps_file(rho_star, T_star, verbose = False):
    """Create LAMMPS parameter file compatible with real unit system.
    
    The non-dimensionalized density rho_start and temperature T_star must be specified."""

    # choose the dimension
    dim = 3

    # define the basic LJ fluid properties
    sigma = 3 * ureg.angstrom # A
    epsilon = 0.1 * ureg.kcal / ureg.mol # kcal/mol
    mass = 1.0 * ureg.g / ureg.mol # g/mol

    # estimate the temperature in Kelvin
    kB = 1.987204259e-3 * ureg.kcal / ureg.mol / ureg.K # kcal/mol/K
    temp_pref = epsilon/kB # temperature prefactor
    T = np.round(temp_pref * T_star, 3) # K

    # tomestep
    time_pref = np.sqrt(mass*sigma**2/epsilon)
    timestep = 0.0025 * time_pref # fs
    timestep = timestep.to(ureg.fs)  # fs

    # volume_single_particle = np.pi * sigma**dim / 6
    required_L = 30
    actual_L = np.int32((required_L / sigma).magnitude)*sigma
    total_volume = actual_L ** dim
    particule_number  = np.int32(rho_star * total_volume / sigma**dim)

    number_density = particule_number / total_volume
    non_dim_number_density = number_density * sigma**3

    if verbose:
        print("n_part = "+str(particule_number))
        print("box dimension = "+str(actual_L))
        print("adim number density:", np.round(non_dim_number_density.magnitude,4))
        print()

    f = open("parameters.lammps", "w")
    f.write("# LAMMPS parameters \n")
    f.write("\n")
    f.write("# Fluid parameters \n")
    f.write("variable mass equal " + str(mass.magnitude) + " # " + str(mass.units) + "\n")
    f.write("variable sigma equal " + str(sigma.magnitude) + " # " + str(sigma.units) + "\n")
    f.write("variable epsilon equal " + str(epsilon.magnitude) + " # " + str(epsilon.units) + "\n")
    f.write("\n")
    f.write("# Simulation parameters \n")
    f.write("variable dt equal " + str(np.round(timestep.magnitude,2)) + " # " + str(timestep.units) + "\n")
    f.write("variable n_part equal " + str(particule_number) + "\n")
    f.write("variable L equal " + str(actual_L.magnitude) + " # " + str(actual_L.units) + "\n")
    f.write("variable T equal " + str(T.magnitude) + " # " + str(T.units) + "\n")
    f.close()

rho_star = 0.85
temperature = 1.1
create_parameter_lammps_file(rho_star,
                             temperature, 
                             verbose = True)
