print("="*17)
print("==CHALLENGER008==")
print("="*17)
print("the purpose of this program is to receive a measurement in metres and convert it to centimetres and millimetres")
print("="*17)

metres = float(input("tipe your measurement in metres: "))
centimetres = metres *100
millimetres = metres *1000

print("the result of the conversion is:")
print("In centimetres the measurement is, {:.0f}cm while in millimetres it is {:.0f}mm".format(centimetres, millimetres))

# print("the result of the conversion is. In centimetres the measurement is,", centimetres, "while in millimetres it is", millimetres)