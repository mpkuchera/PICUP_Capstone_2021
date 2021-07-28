"""
Example python program with PEP-8 documentation

name: example_function.py
author: M.P. Kuchera
date created: 28 July 2021

"""

#imports
import math




# function name: relativistic_energy
def relativistic_energy(mass,velocity):
    """
    Computes a linear fit to find the slope and y-intercept of input data.

    Parameters
    ----------
    mass: FLOAT
        mass of particle in MeV/c^2
    velocity: FLOAT
        velocity of particle as a fraction of c

    Returns
    -------
    energy: FLOAT
       relativistic energy in MeV
        
    """
    v = velocity
    gamma = 1./math.sqrt(1-v**2)
    return gamma*mass


def main():
  m = 0.511 # mass of electron in MeV/c^2
  v = 0.967
  print(relativistic_energy(m,v), "MeV")

if __name__ == "__main__":
  main()
