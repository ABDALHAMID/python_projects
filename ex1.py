# Exercice 1 :
# Soit un environnement contenant deux agent A et B :
#  Ecrire le code de la classe Agent_A ou l’agent A demande à l’agent B de changer sa position
#  Ecrire le code de la classe Agent_B qui calcule sa décision en utilisant l’équation x 2 + log(y3), ou x et
# y sont l’abscisse et l’ordonné de l’agent (rendus d’une manière aléatoire), et lui répond selon la parité
# du résultat (OK ! si pair, NO ! sinon)
#  Ecrire le code la classe Environnement qu’utilise la planification BaseScheduler des agents
#  Lancer votre environnement

import mesa
import random
import math

class Agent_A(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        print("changer la position")

class Agent_B(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.x = random.randint(1, 10)
        self.y = random.randint(20, 200)

    def step(self):
        equ = pow(self.x, 2) + math.log(self.y, 3)
        if int(equ) % 2 == 0:
            print("Ok!")
        else:
            print("No!")

class Enverenement(mesa.Model):
    def __init__(self):
        super().__init__()
        A = Agent_A(1, self)
        B = Agent_B(2, self)
        self.plan = mesa.time.BaseScheduler(self)
        self.plan.add(A)
        self.plan.add(B)

    def step(self):
        self.plan.step()


model = Enverenement()
model.step()
