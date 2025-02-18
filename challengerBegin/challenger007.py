print("="*17)
print("==CHALLENGER007==")
print("="*17)
print("the purpose of this programme is to receive two marks form a studant and calculate their average")
print("="*17)
aprove = 7.5
failed = 5

mark1 = float(input("Type your firs mark: "))
mark2 = float(input("Type your second mark: "))
averageMark = (mark1+mark2)/2

# print("the average between {:.1f} and {:.1f} is {:.1f}".format(mark1, mark2, averageMark))

if averageMark <= failed:
    print("I'm sorry but you didn't achieve the minimum score to pass. Your avarege was {}".format(averageMark))
elif averageMark > failed and averageMark < aprove:
    print ("Unfortunately you didn't achieve the minimum score to pass, but you can try again. Your avarege was {}".format(averageMark))
else:
    print("Congratulations you are aproved. Your avarege is {:.1f}".format(averageMark))



# newAttempt = input("Do you want to repeat your exam? \n If so, press the Y key and then press the Enter key. \n If you want to retake the whole module, press the N key.")
# if newAttempt == Yes:
#     print("Congratulations you have been registered for the next exam.\n You will receive an e-mail with all the information about the date and time of your next exam. ")
# else: 
#     print("Congratulations, you've been enrolled in the next class. You'll receive an e-mail with the start date.")
