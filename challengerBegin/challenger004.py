print("===========================")
print("====C H A L L E N G E R====")
print("===========================")
print("  ")

# This programme aims to capture data entered by the user and show what the primitive type is

userInput = input("Type any information in your keyboard: ")
print("  ")
print("  ")

print("===resultado lógico para saber se é um número===")
print(userInput.isnumeric())
print("==============")

print("===resultado lógico para saber se é uma letra===")
print(userInput.isalpha())
print("==============")

print("===resultado lógico para saber se é um alfanumérico===")
print(userInput.isalnum())
print("==============")

print("===resultado lógico para saber se é uma letra maiúscula===")
print(userInput.isupper())
print("==============")

print("===resultado lógico para saber se é uma letra minuscula===")
print(userInput.islower())
print("==============")

print("===resultado lógico para saber se é um espaço em branco===")
print(userInput.isspace())
print("==============")

print("If the answer is False for all the above results, the data you entered is a special character.")


# backlog when I learn how to use if and else,
# I should update this code so that it checks and tells me what the data type is among all the data types




# print(userInput.isnumeric())
# print(userInput.isalpha())
# print(userInput.isalnum())
# print(userInput.isupper())
# print(userInput.islower())
# print(type(userInput))
# example
# userInput = input("Type n informatio in your keyboard: ")
# print(userInput.isalnum())

# Importante ele só imprime o tipo se eu colocar corretamente o valor, exemplo
# se eu pedir para o usuário digitar um número e ele digitar uma letra vai dar ruim, isso pq
# estou especificando o tipo do dado na captura.
# userInput = float(input("Type n infoormatio in you keyboar: "))
# print(type(userInput))
#
# userInput1 = input("Type n infoormatio in you keyboar: ")
# print(userInput1.isalpha())
#


