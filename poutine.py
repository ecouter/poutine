poutinechoice = input("LBS or KG: ")
if poutinechoice == "LBS":
    poutine = input("Enter your weight in LBS: ")
    poutine = float(poutine)
    poutineweight = 1.3690706
    finalweight = poutine / poutineweight
    print("You are made of " + str(finalweight) + " poutines")
elif poutinechoice == "KG":
    poutine = input("Enter your weight in KG: ")
    poutine = float(poutine)
    poutineweight = 0.621
    finalweight = poutine / poutineweight
    print("You are made of " + str(finalweight) + " poutines")
else:
    print("error")
while True:
    pass