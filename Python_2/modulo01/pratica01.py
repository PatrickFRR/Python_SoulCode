# Crie uma classe animal com atributos e métodos
# Crie uma classe que herde seus atributos, e possuía os seus atributos próprios.
# Crie dois objetos da classe filha.
class Animal:
    def __init__(self, name, large):
        self.name = name
        self.large = large


class Panther (Animal):
    def __init__(self, name, large, sound):
        super().__init__(name, large)
        self.sound = sound


Leon = Panther('Leon', 'Medium', 'Rouge')
Chitara = Panther('Chitara', 'Small', 'Rouge')

print(vars(Leon))
print(vars(Chitara))
