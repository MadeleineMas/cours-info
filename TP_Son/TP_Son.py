####### Importation des bibbliothèques

import matplotlib.pyplot as plt
import numpy as np
#from Ipython.display import Audio,display #ça c'est pr jouer les sons
from scipy.io import wavfile

#######  Questions ########

"""
1 ) On doit avoir 44 100 échantillons pour avoir 1 seconde d'audio

2 ) f=A*np.sin(2*np.pi*phi*t) avec A une amplitude

3 ) """

temps=np.linspace(0,50)
son=np.sin(2*np.pi*temps*440)
plt.plot(temps,son)
plt.show()

# display(Audio(son,44100)) j'ai jamais reussi a télécharger Ipython

#4)

def produitson(fréquence, durée): #on prend en entrée une fréquence qui nous interesse et la durée du son
    temps=np.linspage(0,durée)
    son=np.sin(2*np.pi*temps*fréquence)





