print("="*17)
print("==CHALLENGER006==")
print("="*17)
print("the purpose of this programme is to receive a number and calculate its double, triple and square root")
print("="*17)

num= int(input("Type one number: "))
num2 = num*2
num3 = num*3
num4 = num**(1/2)

print ("the number you entered was {} the double of this number is {}".format(num, num2))
print ("the triple is igual to {} and the square root is {:.2f}".format(num3, num4))

# a formatação {:.2f} representa que só será exibido para o usuário 2 número após o ponto.
# print("the number you entered was", num, "the double of this number is ", num2, "the triple is", num3, "and the square root is ",num4)
