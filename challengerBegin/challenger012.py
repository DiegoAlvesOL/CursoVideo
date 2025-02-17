print("="*17)
print("==CHALLENGER012==")
print("="*17)
print("the purpose of this programme is to receive the price of a product and apply a 5% descont")
print("="*17)

priceProduct = float(input("Enter the valoue of the product: "))
descont =int(input("Enter the desont: "))

descontPrice = (priceProduct/100)*descont
print(descontPrice)
finalPrice = priceProduct-descontPrice

print("The final value of the product is: ",finalPrice)