# Super-heróis são personagens com poderes sobrehumanos. Criados pela imaginação do homem, eles estão sempre em alerta para proteger o mundo dos ataques de mentes cruéis que pretendem dominar o planeta.
# Cada super-herói tem uma origem interessante. Alguns, como o Incrível Hulk, o Capitão América e o Homem de Ferro, surgiram em laboratórios, e eram pessoas comuns antes de adquirirem seus superpoderes a partir de acidentes ou experiências com raios-gama, reações químicas e estudos científicos nos campos da física, engenharia e biologia. Outros, como o Super-Homem e o Lanterna-Verde, vieram de outros planetas. Existem ainda aqueles que se originaram das mitologias, como é o caso do Thor e a Mulher-Maravilha.
# Em quase todas as histórias, o super-herói é chamado para resolver um problema ou enfrentar ameaças de um vilão com um plano maligno. O vilão também é munido de superpoderes mas dificilmente consegue vencer o super-herói, pois os poderes deste são mais fortes.
# Na lista abaixo são citados alguns super-heróis e alguns vilões. A lista apresenta também o nome na vida real e os superpoderes de cada um. Os superpoderes foram categorizados de 1 a 5, sendo 5 o poder mais forte e 1 o poder mais fraco.

class SuperPoder:
    def __init__(self, nome, categoria):
        self.__nome = nome
        self.__categoria = categoria

    def get_nome(self):
        return self.__nome

    def get_categoria(self):
        return self.__categoria



class Personagem:
    def __init__(self, nome, nome_vida_real):
        self.__nome = nome
        self.__nome_vida_real = nome_vida_real
        self.__poderes = []

    def adicionar_super_poder(self, poderes):
        if(len(self.__poderes)<= 3):
            self.__poderes.append(poderes)
        else :
           raise ValueError

    def get_poder_total(self):
        total_poder = 0
        for i in range(len(self.__poderes)):
            total_poder += self.__poderes[i].get_categoria()
        return total_poder 

class SuperHeroi(Personagem):
    def __init__(self, nome, nome_vida_real):
        super().__init__(nome, nome_vida_real)

    def get_poder_total(self):
        return super().get_poder_total() * 1.1
        

class Vilao(Personagem):
    def __init__(self, nome, nome_vida_real, tempo_de_prisao):
        super().__init__(nome, nome_vida_real)
        self.tempo_de_prisao = tempo_de_prisao

class Confronto:
    def lutar(self, superheroi, vilao):
        if (superheroi.get_poder_total() > vilao.get_poder_total()):
            return 1
        elif (superheroi.get_poder_total() < vilao.get_poder_total()):
            return 2
        else :
            return 0