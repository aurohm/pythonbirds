class Pessoa:
    olhos = 2 # atribute default ou atributo de classe

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
    velton.sobrenome = 'Moura'
    del velton.filhos
    velton.olhos = 1
    del velton.olhos
    print(velton.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(velton.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(velton.olhos), id(renzo.olhos))
