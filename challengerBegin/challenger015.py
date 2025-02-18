print("="*17)
print("==CHALLENGER015==")
print("="*17)
print("The purpose of this programme is to calculate how much I have to pay for a rental car,\ngiven that the daily rate for the car is 60 euros and 0.15 cents per kilometre driven.")
print("="*17)

daily = 60.0
km = 0.15

daily2 = int(input("How many days did you keep the car? "))
km2 = float(input("How many kilometres have you travelled? "))

totalDaily = daily*daily2
totalKm = km*km2
result = totalDaily+totalKm

print("the daily rate was U${:.2f} and the kilometre rate was U${:.2f}. The total due is U${:.2f}".format(totalDaily, totalKm, result))