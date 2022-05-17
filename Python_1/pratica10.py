# 1-Deve se criar 5 funções diferentes,sendo elas somar,subtrair,dividir,multiplicar e listar.

def operation1(x, y):
    addition = x + y;
    print(addition);

def operation2(x, y):
    subtration = x - y;
    print(subtration);

def operation3(x, y):
    multiplication = x * y;
    print(multiplication);

def operation4(x, y):
    division = x / y;
    print(division);


# 2-Deve se criar um MENU com if else sendo que o usuário escolha qua função deve acessar.
menu = int(input(
    "Enter your option opertation:\n 1 - addition\n 2 - subtration\n 3 - multiplication\n 4 - division\n 5 - list\n "));
if menu == 1:
    number1 = float(input("Enter first number: "));
    number2 = float(input("Enter second number: "));
    operation1(number1, number2);
elif menu == 2:
    number1 = float(input("Enter first number: "));
    number2 = float(input("Enter second number: "));
    operation2(number1, number2);
elif menu == 3:
    number1 = float(input("Enter first number: "));
    number2 = float(input("Enter second number: "));
    operation3(number1, number2);
elif menu == 4:
    number1 = float(input("Enter first number: "));
    number2 = float(input("Enter second number: "));
    operation4(number1, number2);

  