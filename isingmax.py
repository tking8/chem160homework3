from random import random,choice
from math import exp
Temp=2.3              # Temperature
n=20                  # Sites per edge for n x n system
n2=n*n                # Precalculate n*n
nlist=list(range(n))  # List of sites 
ntrials=200000        # Number Trials 
nequil=100000         # Equilibration steps

# Initialize sums for maximum and minimum
Emax=-5.0
Emin=+5.0

# Create initial matrix of spins all spin up
spins=[[1 for i in range(n)] for j in range(n)]

# Run simulation
for trial in range(1,(ntrials+nequil+1)):
    # Randomly pick a site
    i=choice(nlist)
    j=choice(nlist)

    #Calculate the change in energy if we flip this spin
    deltaE=2.*(spins[i][j]*\
               (spins[i][(j+1)%n]+spins[i][(j-1+n)%n]+\
                 spins[(i+1)%n][j]+spins[(i+-1+n)%n][j]))

    #Flip the spin using Metropolis MC
    if exp(-deltaE/Temp)>random():   
        spins[i][j]=-spins[i][j]
    else:
        deltaE=0.0

    # Calculate system energy ONCE 
    if trial == nequil:
        energy=0.0  
        for i in range(n):
            for j in range(n):
                energy-=(spins[i][j]*
                         (spins[i][(j+1)%n]+spins[i][(j-1+n)%n]+\
                          spins[(i+1)%n][j]+spins[(i+-1+n)%n][j]))
        energy+=2*deltaE/n2
    
    # Check for new minimum or maximum
        if energy > Emax:
            Emax=energy
        if energy < Emin:
            Emin=energy

print('%10.6f %10.6f'%(Emin, Emax))
