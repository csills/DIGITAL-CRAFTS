totalAmount = float(raw_input("Enter Total Bill Amount:$ "))
serviceQuality = raw_input("Was the Service Quality: Good, Fair, or Bad?")
serviceQualityValues = ["Good", "Fair", "Bad"]


if serviceQuality == "Good":
    tipPercentage = totalAmount * .20
elif serviceQuality == "Fair":
    tipPercentage = totalAmount * .15
elif serviceQuality == "Bad":
    tipPercentage = totalAmount * .10

split = int(raw_input("How many people will be splitting the bill?"))
splitCost = (totalAmount + tipPercentage) / split
print "Each person owes: $%d." % (splitCost)