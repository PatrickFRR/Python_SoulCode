# 1-Crie um dicionário contendo dias da semanas sendo dia1,dia2,dia3...as chaves e o dia seu valor.
#  Ex: “dia1”: “domingo”.2-Remova dois dos últimos dias da semana.
diccionary = {"day1": "Sunday", "day2": "Monday", "day3": "Tuesday", "day4": "Wednesday", "day5": "Tursday", "day6": "Friday", "day7": "Saturday"};
print(diccionary);
# 3-Remova segunda-feira pela sua chave.
diccionary.popitem()
del(diccionary["day2"])
# 4-Imprima chaves e valores do dicionário. 
print(diccionary.keys())
print(diccionary.values())
# 5-Imprima o dicionário final.
print(diccionary)