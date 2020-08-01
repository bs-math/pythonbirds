class Pessoa:
    olhos = 2 #atributo de classe

    def __init__(self, *filhos, nome=None, idade=0): #atributos de instância
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    math = Pessoa(nome='Math', idade=26)
    luciano = Pessoa(math, nome='Luciano', idade=80)
    print(Pessoa.cumprimentar(luciano))     #mostram que todos os
    print(id(luciano))                      #objetos usados aqui são
    print(luciano.cumprimentar())           #o mesmo objeto
    print(luciano.nome)
    for filho in luciano.filhos:            #mostra cada filho, caso contrário mostraria apenas
        print(filho.nome)                   #um código de obeto

    luciano.sobrenome = 'Ramalho'           #atributo dinânico
    print(luciano.__dict__)                 #mostra os atributos do objeto
    print(math.__dict__)
    print(Pessoa.olhos) # Pode mostrar o atributo de classe, mas não os de instância
    print(math.olhos)
