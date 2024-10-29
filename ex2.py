# Exercice 2 :
# Soit un environnement contenant deux agents rationnels, chacun a un durée de fonctionnement d'une manière
# séquentielle (le 1er agent entre et fait son travail et sort pour céder le reste du travaille au 2
# eme agent).
#  Le 1
# er agent travaille pour 8 heures et effectue un calcul (incrémente une variable i par 1)
#  Le 2
# eme agent fonctionne pour une durée de 9 heures et incrémente la dernière valeur calculée, par
# l'agent, par 1

import mesa

class Agent_A(mesa.Agent):
    def __init__(self, unique_id, model, tash):
        super().__init__(unique_id, model)
        self.tash = tash

    def step(self):
        self.tash += 1
        print(self.tash)

class Agent_B(mesa.Agent):
    def __init__(self, unique_id, model, tash):
        super().__init__(unique_id, model)
        self.tash = tash

    def step(self):
        self.tash += 2
        print(self.tash)

class Environment(mesa.Model):
    def __init__(self):
        super().__init__()
        self.tash = 0
        self.A = Agent_A(0, self, self.tash)
        self.plan = mesa.time.BaseScheduler(self)
        self.plan.add(self.A)

    def step(self):
        for i in range(8):
            self.plan.step()
        self.plan.remove(self.A)
        self.B = Agent_B(1, self, self.tash)
        self.plan.add(self.B)
        for i in range(9):
            self.plan.step()



env = Environment()
env.step()