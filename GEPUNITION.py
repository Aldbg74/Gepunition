# GE-PUNITION
#GEPUNITION est une nouvelle vertion de GEMOT
#Cette vertion est axée sur la gestion de punition et de devoir
#Elle est plus réservé a un usage de la vie-scolaire

# Commande pour importer la fonction random et pour permettre un
#choix aléatoire entre les 10 punition
import random
import time
devoirs = random.randint(1, 6)

#On lance le programe
while True :
    print("G E P U N I T I O N")
    print("")
    print("Génération de la punition")
    time.sleep(5)

    if devoirs == 1 :
        print("Copier des lignes")
        break

    if devoirs == 2:
        print("Travail sur le pourquoi de la mauvaise action")
        break

    if devoirs == 3:
        print("Travail sur un sujet de votre choix")
        break

    if devoirs == 4:
        print("Changement de place")
        break

    if devoirs == 5:
        print("Exposé sur un sujet de votre choix")
        break

    if devoirs == 6:
        print("Un avertissement devrait suffire")
        break
