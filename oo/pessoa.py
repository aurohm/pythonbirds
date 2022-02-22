class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(id(p))
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())