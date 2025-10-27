##########################################
# Foisy, Emmanuelle, <6297150>
##########################################
import random
#fonction qui génère 10 températures entre 20 et 35
temperature= round(random.uniform(20,35),1)
def question_1(temperature):
    for i in range(1,11):
        temperature = round(random.uniform(20, 35), 1)
        print("Jour",i,":",temperature)
        if temperature>=24 and temperature<=30 :
            print("OK")
        elif temperature <24:
            print("Trop froid")
        else:
            print("Trop chaud")
    print("Fin")

#appel de la fonction
question_1(temperature)


import random
import matplotlib.pyplot as plt
import numpy as np

population_initiale= int(input("Population initiale:"))

def question_2(population_initiale):
    heures=0
    for i in range(0,10+1):
        population_initiale+=np.pi/1.5
        heures+=1
        print(population_initiale)
        plt.figure(figsize=(2, 2))
        plt.plot(heures, population_initiale, marker='*',color='blue')
        plt.plot(population_initiale=50000, linestyle='--',color='red')
        plt.xlabel("heures")
        plt.ylabel("population")
        plt.title("Croissance bactérienne")
        plt.grid()
        plt.show()

question_2(population_initiale)
#à chaque fois que l'heure augmente de 1, on ajoute np.pi/1.5 à la quantité initiale de la population
