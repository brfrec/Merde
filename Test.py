fron FonctionDeTest import *

print("Veux tu jouer avec moi ?")
choixJouerAvecMoi = int(input"\n1 - OUI\n2 - NON")
if choixJouerAvecMoi == 1:
    oui()
elif choixJouerAvecMoi == 2:
    non()
else:
    print("J'ai pas demande ça")

