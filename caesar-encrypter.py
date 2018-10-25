inputFileName = input("Enter the file to encrypt: ")
key = int(input("Enter the numeric shift key: "))
outputFileName = input("Enter the file name to write to: ")

inputFile = open( inputFileName, "r")
outputFile = open( outputFileName, "w")

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
shiftedStart = alphabet[len(alphabet) - key:]
shiftedEnd = alphabet[:len(alphabet) - key]
shiftedAlphabet = shiftedStart + shiftedEnd


readTexts = inputFile.readlines()


for line in readTexts:
    singleLine = line.strip()
    encryptedMessage = ""
    for character in singleLine:
       letterIndex = alphabet.find(character)
       encryptedCharacter = shiftedAlphabet[letterIndex]
       encryptedMessage = encryptedMessage + encryptedCharacter
   #print("{0} -> {1}".format(character, encryptedCharacter))
    print(encryptedMessage, file=outputFile)
    
print("The encrypted message is: {0}".format(encryptedMessage))
outputFile.close()
inputFile.close()
print("Done writing encrypted message to file{0}".format(outputFileName))