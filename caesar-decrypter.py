#it is necessary to write separate decryptor for new encryptor.
#old decryptor could only handle one line at a time, making it not useful for multi line text
#use of embedded for loop seperated each line out for individual decryption
#tried to put multi line text into decryptor, came back with only one line decrypted
inputFileName = input("Enter the file name to decrypt: ")
key = int(input("Enter your shift key: "))

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
shiftedStart = alphabet[len(alphabet) - key:]
shiftedEnd = alphabet[:len(alphabet) - key]
shiftedAlphabet = shiftedStart + shiftedEnd

inputFile = open(inputFileName, "r")

textSequence = inputFile.readlines()


for line in textSequence:
    singleLine = line.strip()
    decryptedMessage = ""
    for character in singleLine:
        letterIndex = shiftedAlphabet.find(character)
        decryptedCharacter = alphabet[letterIndex]
        decryptedMessage = decryptedMessage + decryptedCharacter
    print(decryptedMessage)

print("Your decrypted message is shown above!")

inputFile.close()
    
    