
import random

def roll_dice():
    return random.randint(1, 100)

def play_game():
    print("Bienvenue dans le jeu de dés à 100 faces !")
    fail_count = 0
    while True:
        input("Appuyez sur Entrée pour lancer le dé...")
        result = roll_dice()
        print("Vous avez obtenu :", result)
        if result == 100:
            print("Félicitations, vous avez gagné !")
            print("Fails : ", fail_count)
            break
        else:
            fail_count += 1

# Démarrer le jeu
play_game()
