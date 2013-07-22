# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    pop300 = []
    pop150 = []
    pop75 = []
    pop0 = []
    viruses = []
    for i in range(100):
        viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.005))
    for trial in range(numTrials):
        patient = TreatedPatient(viruses[:], 1000)
        for timestep in range(300):
            patient.update()
        patient.addPrescription('guttagonol')
        for timestep in range(150):
            patient.update()
        pop300.append(patient.getTotalPop())
        print "1-"+str(trial)
    for trial in range(numTrials):
        patient = TreatedPatient(viruses[:], 1000)
        for timestep in range(150):
            patient.update()
        patient.addPrescription('guttagonol')
        for timestep in range(150):
            patient.update()
        pop150.append(patient.getTotalPop())
        print "2-"+str(trial)
    for trial in range(numTrials):
        patient = TreatedPatient(viruses[:], 1000)
        for timestep in range(75):
            patient.update()
        patient.addPrescription('guttagonol')
        for timestep in range(150):
            patient.update()
        pop75.append(patient.getTotalPop())
        print "3-"+str(trial)
    for trial in range(numTrials):
        patient = TreatedPatient(viruses[:], 1000)
        patient.addPrescription('guttagonol')
        for timestep in range(150):
            patient.update()
        pop0.append(patient.getTotalPop())
        print "4-"+str(trial)

    num300 = 0.0
    num150 = 0.0
    num75 = 0.0
    num0 = 0.0
    for i in range(numTrials):
        if pop300[i] <= 50:
            num300 += 1
        if pop150[i] <= 50:
            num150 += 1
        if pop75[i] <= 50:
            num75 += 1
        if pop0[i] <= 50:
            num0 += 1
    print "Cured % for 300 = ", str(num300), str(num300/numTrials)
    print "Cured % for 150 = ", str(num150), str(num150/numTrials)
    print "Cured % for 75 = ", str(num75), str(num75/numTrials)
    print "Cured % for 0 = ", str(num0), str(num0/numTrials)
        
    pylab.figure(1)
    pylab.subplot(2,2,1)
    pylab.hist(pop300,10, label = "300")

    pylab.subplot(2,2,2)
    pylab.hist(pop150,10, label = "150")

    pylab.subplot(2,2,3)
    pylab.hist(pop75,10, label = "75")

    pylab.subplot(2,2,4)
    pylab.hist(pop0,10, label = "0")
    pylab.show()

#simulationDelayedTreatment(200)




#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    pop300 = []
    pop150 = []
    pop75 = []
    pop0 = []
    viruses = []
    for i in range(100):
        viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005))
# simulation with delay 300
    for trial in range(numTrials):
        patient = TreatedPatient(viruses[:], 1000)
        for timestep in range(150):
            patient.update()
        patient.addPrescription('guttagonol')
        for timestep in range(300):
            patient.update()
        patient.addPrescription('grimpex')
        for timestep in range(150):
            patient.update()
        pop300.append(patient.getTotalPop())
        print "1-"+str(trial)

# simulation with delay 150
    for trial in range(numTrials):
        patient = TreatedPatient(viruses[:], 1000)
        for timestep in range(150):
            patient.update()
        patient.addPrescription('guttagonol')
        for timestep in range(150):
            patient.update()
        patient.addPrescription('grimpex')
        for timestep in range(150):
            patient.update()
        pop150.append(patient.getTotalPop())
        print "2-"+str(trial)

# simulation with delay 75
    for trial in range(numTrials):
        patient = TreatedPatient(viruses[:], 1000)
        for timestep in range(150):
            patient.update()
        patient.addPrescription('guttagonol')
        for timestep in range(75):
            patient.update()
        patient.addPrescription('grimpex')
        for timestep in range(150):
            patient.update()
        pop75.append(patient.getTotalPop())
        print "3-"+str(trial)

# simulation with delay 0
    for trial in range(numTrials):
        patient = TreatedPatient(viruses[:], 1000)
        for timestep in range(150):
            patient.update()
        patient.addPrescription('guttagonol')
        patient.addPrescription('grimpex')
        for timestep in range(150):
            patient.update()
        pop0.append(patient.getTotalPop())
        print "4-"+str(trial)

    num300 = 0.0
    num150 = 0.0
    num75 = 0.0
    num0 = 0.0
    for i in range(numTrials):
        if pop300[i] <= 50:
            num300 += 1
        if pop150[i] <= 50:
            num150 += 1
        if pop75[i] <= 50:
            num75 += 1
        if pop0[i] <= 50:
            num0 += 1
    print "Cured % for 300 = ", str(num300), str(num300/numTrials)
    print "Cured % for 150 = ", str(num150), str(num150/numTrials)
    print "Cured % for 75 = ", str(num75), str(num75/numTrials)
    print "Cured % for 0 = ", str(num0), str(num0/numTrials)
        
    pylab.figure(1)
    pylab.subplot(2,2,1)
    pylab.hist(pop300,10, label = "300")

    pylab.subplot(2,2,2)
    pylab.hist(pop150,10, label = "150")

    pylab.subplot(2,2,3)
    pylab.hist(pop75,10, label = "75")

    pylab.subplot(2,2,4)
    pylab.hist(pop0,10, label = "0")
    pylab.show()

simulationTwoDrugsDelayedTreatment(200)
