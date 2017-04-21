import watsonTone

inputFile = open("pathOfInput", "rb")
outputFile = open("pathOfOutput", "wb")
watsonTone.getTones(inputFile, outputFile)
