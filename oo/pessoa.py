class Pessoa:
    olhos = 2  # atributo de classe

    def __init__(self, *filhos, nome=None, idade=0):  # atributos de instância
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod  # Decorator (começam com @ e ficam acima de funções e métodos)
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):  # Para acessar dados da própria classe
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    math = Pessoa(nome='Math', idade=26)
    luciano = Pessoa(math, nome='Luciano', idade=80)
    print(Pessoa.cumprimentar(luciano))  # mostram que todos os
    print(id(luciano))  # objetos usados aqui são
    print(luciano.cumprimentar())  # o mesmo objeto
    print(luciano.nome)
    for filho in luciano.filhos:  # mostra cada filho, caso contrário mostraria apenas
        print(filho.nome)  # um código de obeto

    luciano.sobrenome = 'Ramalho'  # atributo dinânico
    print(luciano.__dict__)  # mostra os atributos do objeto
    print(math.__dict__)
    print(Pessoa.olhos)  # Pode mostrar o atributo de classe, mas não os de instância
    print(math.olhos)
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
