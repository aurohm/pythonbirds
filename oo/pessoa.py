class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 29, sexo = 'Masculino'):
        self.sexo = sexo
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    velton = Pessoa(renzo, nome='Velton')
    print(id(velton))
    print(Pessoa.cumprimentar(velton))
    print(velton.cumprimentar())
    print(velton.nome)
    print(velton.idade)
    print(velton.sexo)
    #print(velton.filhos)
    for filho in velton.filhos:
        print(filho.nome)