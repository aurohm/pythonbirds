"""
Você vai criar uma classe que vai possuir dois
atributos compostos por outras duas classes:

1) Motor
O motor terá a responsabilidade de controlar a
velocidade. Ele oferece os seguintes atributos:

a) Atributo de dado velocidade
b) Método acelear, que deverá incrementar a vel
de uma unidade
c) Método frear que deverá decrementar a vel em
duas unidades

2) Direção
A direção terá a responsabilidade de controlar a
direção. Ela oferece os seguintes atributos:

a) Valor de direção com valores possíveis:
Norte, Sul, Leste, Oeste
  N
O   L
  S
b) Método girar_a_direita
c) Método girar_a_esquerda

        Exemplo:
        # Testando motor
        >>> motor = Motor()
        >>> motor.velocidade
        0
        >>> motor.acelerar()
        >>> motor.velocidade
        1
        >>> motor.acelerar()
        >>> motor.velocidade
        2
        >>> motor.acelerar()
        >>> motor.velocidade
        3
        >>> motor.frear()
        >>> motor.velocidade
        1
        >>> # Testando Direção
        >>> direcao = Direcao()
        >>> direcao.valor
        'Norte'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Leste'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Sul'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Oeste'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Norte'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Oeste'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Sul'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Leste'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Norte'
        >>> carro = Carro(direcao, motor)
        >>> carro.calcular_velocidade()
        0
        >>> carro.acelerar()
        >>> carro.calcular_velocidade()
        1
        >>> carro.frear()
        >>> carro.calcular_velocidade()
        2
        >>> carro.frear()
        >>> carro.calcular_velocidade()
        0
        >>> carro.calcular_direcao()
        'Norte'
        >>> carro.girar_a_direita()
        >>> carro.calcular_direcao()
        'Leste'
        >>> carro.girar_a_esquerda()
        >>> carro.calcular_direcao()
        'Norte'
        >>> carro.girar_a_esquerda()
        >>> carro.calcular_direcao()
        'Oeste'
"""

NORTE = 'Norte'
LESTE = 'Leste'
OESTE = 'Oeste'
SUL = 'Sul' # crtl + shift + u

class Direcao:
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

"""        if self.valor == NORTE:
            self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = NORTE"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        #self.velocidade = max(0, self.velocidade)
