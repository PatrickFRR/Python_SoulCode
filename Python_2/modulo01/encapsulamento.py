class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        #atributos com duplo _ são privados e não aparecem como atributos visivéis para o usuário
        self.__salario =  0 # private
        self.__horas_trabalhadas = 0 #private

    @property # Estrutura de segurança 
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        raise ValueError("Impossivel alterar salario diretamente. Use a funcao calcula_salario().")

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada


jose = Funcionario('José', 'Professor', 50)
jose.salario = 100000 # Este código dará um erro, pois _salario está encapsulado, ou seja, privado.
