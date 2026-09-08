import numpy as np
import matplotlib.pyplot as plt
image = np.empty((91,91,3), dtype=np.uint8)
image[:]=[0,0,0]
image[: : 10]= [0,0,255] #on colorise les lignes en bleu
image[:,::10]=[0,0,255] # on colorise les colonnes en bleu
#plt.imshow(image)
#plt.show()
#print (image[0,0], image[-1,-1])




## Lecture d'une image de couleur ##############################################################

arbre = plt.imread("les-mines.jpg") # on lit l'image en la stockant
arbre2 = arbre.copy()
print (bool(arbre.flags.writeable),bool(arbre2.flags.writeable)) #on check si c'est writeable ou pas
plt.imshow(arbre)
#plt.show()
print(type(arbre2)) # donne le type de l'image
print("dimension=",arbre2.ndim) # donne les dimensiosn de l'image
print("hauteur, largeur:",arbre2.shape[:2]) # done la hauteur, largeur
print(arbre2.itemsize) #octets par valeur 
print(arbre2.dtype) #donne type octet des pixels
print(arbre2.min(), arbre2.max()) #donne  les max et le min du tableau
plt.imshow(arbre2[:10, :10]) # affiche le rectangle de 10 du haut a gauche
#plt.show()




##accès à des parties d'image####################################################################

for i in (2,5,10,20):
    plt.imshow(arbre2[::i,::i])
    #plt.show()

def isolerectangle(l,c):
    n,p = arbre2.shape[:2]
    return arbre2[n/2-l : n/2+l , p/2-c : p/2+c]
plt.show(isolerectangle(100,200))













