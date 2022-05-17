# 1-Crie uma string contendo o alfabeto com letras maiúsculas separado por espaços.
alpha =  "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z";

# 2-Percorra e imprima essa string com enumerate.
for k, v, in enumerate(alpha):
    print(k,v);

# 3-Substitua os espaços por traço. “-” e imprima para o usuário.
print(alpha.replace(" ", "-"));