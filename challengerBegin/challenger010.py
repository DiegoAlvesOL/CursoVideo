print("="*17)
print("==CHALLENGER010==")
print("="*17)
print("the purpose of this programme is to receive a value in real and convert it into dollars")
print("="*17)

balance = float(input("please enter how much mooney do you have: "))
dollar = float(input("inform the dollar amount: "))

conversionResult = balance / dollar

print("With R${:.2f} you can buy U${:.2f}".format(balance, conversionResult))

