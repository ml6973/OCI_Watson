from OCI_Watson import preProcessor
from OCI_Watson import postProcessor
from OCI_Watson import watsonTone

#Add a counter to the header file
inputFile = open("testHeader.csv", "rb")
outputFile = open("pathToCountedHeaderFile", "wb")
preProcessor.addHeaderCounter(inputFile, outputFile)

#Add a counter to the body file
inputFile = open("testBody.csv", "rb")
outputFile = open("pathToCountedBodyFile", "wb")
preProcessor.addBodyCounter(inputFile, outputFile)

#Get the tones of the headers
inputFile = open("pathToCountedHeaderFile", "rb")
outputFile = open("pathToHeaderOutputFile", "wb")
watsonTone.getHeaderTones(inputFile, outputFile)

#Get the tones of the bodies
inputFile = open("pathToCountedBodyFile", "rb")
outputFile = open("pathToBodyOutputFile", "wb")
watsonTone.getBodyTones(inputFile, outputFile)

#Merge the outputs of the previous two functions into one file
headerFile = open("pathToHeaderOutputFile", "rb")
bodyFile = open("pathToBodyOutputFile", "rb")
outputFile = open("pathToFinalOutputFile", "wb")
postProcessor.mergeTables(headerFile, bodyFile, outputFile)
