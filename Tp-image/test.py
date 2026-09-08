import numpy as np
import matplotlib.pyplot as plt
image = np.empty((91,91,3), dtype=np.uint8)
image[:]=[0,0,0]
image[: : 10]= [0,0,255] #on colorise les lignes en bleu
image[:,::10]=[0,0,255] # on colorise les colonnes en bleu
#plt.imshow(image)
#plt.show()
#print (image[0,0], image[-1,-1])




## Lecture d'une image de couleur ###################################################################

arbre = plt.imread("les-mines.jpg") # on lit l'image en la stockant
arbre2 = arbre.copy()
print (bool(arbre.flags.writeable),bool(arbre2.flags.writeable)) #on check si c'est writeable ou pas
#plt.imshow(arbre)
#plt.show()
print(type(arbre2)) # donne le type de l'image
print("dimension=",arbre2.ndim) # donne les dimensiosn de l'image
print("hauteur, largeur:",arbre2.shape[:2]) # done la hauteur, largeur
print(arbre2.itemsize) #octets par valeur 
print(arbre2.dtype) #donne type octet des pixels
print(arbre2.min(), arbre2.max()) #donne  les max et le min du tableau
#plt.imshow(arbre2[:10, :10]) # affiche le rectangle de 10 du haut a gauche
#plt.show()




##accès à des parties d'image########################################################################

#for i in (2,5,10,20):
    #plt.imshow(arbre2[::i,::i])
    #plt.show()

def isolerectangle(l,c):
    n,p = arbre2.shape[:2]
    return arbre2[n//2-l//2 : n//2+l//2 , p//2-c//2 : p//2+c//2] #
#plt.imshow(isolerectangle(100,200))
#plt.show()

##Canaux RGB de l'image #############################################################################

arbreR = arbre2[:,:,0]
arbreG = arbre2[:,:,1]
arbreB = arbre2[:,:,2]
#plt.imshow(arbreR, cmap="Reds")
#plt.show()
#plt.imshow(arbreG, cmap="Greens")
#plt.show()
#plt.imshow(arbreB, cmap="Blues")
#plt.show()

arbre3=arbre2.copy()
arbre3[-200 :,-200 :]=[255,255,255]
arbre3[-200: : 2, -200 : ]=[255,0,0]
#plt.imshow(arbre3[-20:,-20:])
#plt.show()

            # Transparence
n,p=arbre2.shape[:2]
arbreopac = np.empty((n,p,4), dtype=np.uint8)

arbre4 = arbre.copy()
arbreopac[::,::,:3]=arbre4
arbreopac[:,:,3]=128
#plt.imshow(arbreopac)
#plt.show()

##image en niveau de gris en float ##########################################################################

arbrefloat = np.empty((n,p,3), dtype=np.uint8) # on crée les images que on modifiera en gris
arbrefloat=arbre2/255.0
arbrefloat1=arbrefloat.copy()
arbregris = np.empty((n,p,3), dtype=np.uint8)
arbregris=arbre2/255.0


arbrefloat[:,:,0] = arbrefloat[:,:,0]/3+arbrefloat[:,:,1]/3+arbrefloat[:,:,2]/3 # on fait la premeire moyenne
arbrefloat[:,:,1] = arbrefloat[:,:,0]
arbrefloat[:,:,2] = arbrefloat[:,:,0]
#plt.imshow(arbrefloat)
#plt.show()

arbregris[:,:,0] = 0.299*arbrefloat1[:,:,0] +0,587*arbrefloat1[:,:,1] +0.114*arbrefloat1[:,:,0] 
arbregris[:,:,1] = arbregris[:,:,0]
arbregris[:,:,2] = arbregris[:,:,0] # on fait la moyenne avec la formule
#plt.imshow(arbrefloat)
#plt.show()












