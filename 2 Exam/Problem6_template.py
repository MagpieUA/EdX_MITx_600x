import random
import pylab
import numpy as np

#Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    global CURRENTRABBITPOP
    numRabbits = CURRENTRABBITPOP
    for rabbit in range(numRabbits):
        rand = random.random()
        if rand <= (1 - float(CURRENTRABBITPOP)/MAXRABBITPOP):
            CURRENTRABBITPOP += 1
        
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    numFoxes = CURRENTFOXPOP
    for fox in range(numFoxes):
        if CURRENTRABBITPOP > 10:
            if random.random() <= float(CURRENTRABBITPOP)/MAXRABBITPOP:
                CURRENTRABBITPOP -= 1
                if random.random() <= 1.0/3:
                    CURRENTFOXPOP += 1
            else:
                if random.random() <= 9.0/10:
                    CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)
    
numSteps = 100
(rabbit_populations, fox_populations) = runSimulation(numSteps)
pylab.figure(1)
pylab.plot(range(numSteps),rabbit_populations)
pylab.plot(range(numSteps),fox_populations)
coeff = np.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
pylab.plot(np.polyval(coeff, range(len(rabbit_populations))))
pylab.show()
