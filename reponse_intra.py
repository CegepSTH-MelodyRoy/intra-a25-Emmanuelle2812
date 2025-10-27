##########################################
# Foisy, Emmanuelle, <6297150>
##########################################
import random
#fonction qui génère 10 températures entre 20 et 35
temperature= round(random.uniform(20,35),1)
def question_1(temperature):
    for i in range(1,11):
        print("Jour",i,":",temperature)
        if temperature>=24 or temperature<=30:
            print("OK")
        elif temperature <24:
            print("Trop froid")
        else:
            print("Trop chaud")
    print("Fin")

#appel de la fonction
question_1(temperature)
#la fonction devrait avoir dix températures différentes, mais la mienne affiche 10 fois la même
#je ne comprends pas pourquoi le message est toujours OK, même si je l'ai mis dans un if/elif/else

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
        plt.plot([0, 10], [50000], linestyle='--',color='red')
        plt.xlabel("heures")
        plt.ylabel("population")
        plt.title("Croissance bactérienne")
        plt.grid()
        plt.show()

question_2(population_initiale)
