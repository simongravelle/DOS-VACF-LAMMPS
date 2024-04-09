import numpy as np
from scipy import constants as cst

def calculate_autocorr(X, N):
    """Calculate autocorrelation."""
    return np.correlate(X, X, mode='full')[-N:]

def detect_dump(file):
    """Read LAMMPS dump and return the atom number and number of frames."""
    content = open(file, 'r')
    cpt = 0
    cpt_number = -1
    cpt_atom = -1
    cpt_frame = -1
    steps_array = []
    n_frames = 0
    for line in content:
        if len(line.split(" ")) > 1:
            if 'NUMBER' in line.split(" ")[1]:
                cpt_number = cpt + 1
            if 'TIMESTEP' in line.split(" ")[1]:
                n_frames += 1
                cpt_frame = cpt + 1
            if 'ATOMS' in line.split(" ")[1]:
                cpt_atom = cpt + 1
        if cpt == cpt_number:
            n_atoms = np.int32(line[:-1])
        if cpt == cpt_atom:
            n_columns = len(line.split())
        if cpt == cpt_frame:
            steps_array.append(np.int32(line[:-1]))
        cpt += 1
    content.close()
    return n_atoms, n_frames, n_columns, steps_array

def read_dump(file):
    """Read velocity from lammpstrj dump."""
    n_atoms, n_frames, n_columns, steps_array = detect_dump(file)
    content = open(file,'r')
    data = np.ndarray((n_atoms, n_columns-1, n_frames),
                      dtype=float)
    masses = np.ndarray(n_atoms, dtype=float)
    cpt = 0
    while (cpt < n_frames):
        for i in range(3):
            _ = content.readline()
        n_atoms_bis = np.int32(content.readline())
        assert n_atoms_bis == n_atoms
        for i in range(5):
            _ = content.readline()        
        for a in range(n_atoms):
            line = content.readline().strip('\n').split()
            data[a, :, cpt] = line[1:]
            masses[a] = line[0]
        cpt += 1
    content.close()
    printing_period = np.diff(steps_array)[0]
    return data, n_atoms, n_frames, n_columns, printing_period, masses

def calculate_fft(time, input):
    """
    Calculate the Fourier transform of an array.

    Wrap function that takes the data in real space with
    columns time, frequency and returns the data in Fourier space
    with columns frequency, signal

    Units in : ps, signal
    Units out : Hz, s*signal

    **Parameters**

    data : numpy.ndarray

    **Returns**

    np.ndarray
    """
    dt = (time[1] - time[0]) * cst.pico  # second
    freq = np.fft.rfftfreq(len(input), dt)
    output = np.fft.rfft(input) * dt * 2
    return np.vstack((freq, np.abs(output))).T