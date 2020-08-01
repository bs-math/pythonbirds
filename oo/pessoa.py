class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 0):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    math = Pessoa(nome='Math', idade = 26)
    luciano = Pessoa(math, nome='Luciano', idade = 80)
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    for filho in luciano.filhos:
        print(filho.nome)
