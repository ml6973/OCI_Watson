import watsonTone

inputFile = open("pathOfInput", "rb")
outputFile = open("pathOfOutput", "wb")
watsonTone.getHeaderTones(inputFile, outputFile)

inputFile = open("pathOfInput", "rb")
outputFile = open("pathOfOutput", "wb")
watsonTone.getBodyTones(inputFile, outputFile)
