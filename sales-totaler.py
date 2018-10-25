salesFileName = input("Enter sales file name: ")
outputFileName = input("Enter name for total sales file")

salesFile = open(salesFileName, "r")
outputFile = open(outputFileName, "w")


sales = salesFile.readlines()

for number in sales:
    numbers = number.strip().split(" ")
    firstNumber = numbers[0]
    secondNumber = numbers[1]
    firstAdd = float(firstNumber[1:])
    secondAdd = float(secondNumber[1:])
    totalPerLine = float(firstAdd + secondAdd)
    firstAdd = str(firstAdd)
    secondAdd = str(secondAdd)
    totalPerLine = str(totalPerLine)
    print("${0} ${1} ${2}".format(firstAdd.rjust(8), secondAdd.rjust(8), totalPerLine.rjust(8)), file=outputFile)
    
print("Done writing sales to {0}".format(outputFileName))    

#print(sales)
salesFile.close()
outputFile.close()
