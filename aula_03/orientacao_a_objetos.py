class Carro:
    # Metodo para iniciar o objecto
    def __init__(self, nome):
        # atributo de dados do objecto
        self.name = nome

    def acelerar(self):
        return id(self)


if __name__ == '__main__':

    monza = Carro('Monza')
    print(id(monza), monza.acelerar(), Carro.acelerar(monza))
    punto = Carro('Punto')
    print(id(punto), punto.acelerar(), Carro.acelerar(punto))
    print(monza.name)
    punto.name = 'Punto'
    print(punto.name)
