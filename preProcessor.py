import csv

def addHeaderCounter(inputFile, outputFile):
   inputReader = csv.reader(inputFile)
   outputWriter = csv.writer(outputFile)
   firstValue = next(inputReader)
   if not firstValue == ['Headline', 'Body ID', 'Stance']:
      raise ValueError("The input file's first row does not comform to the documented format")
   outputWriter.writerow( ('HeaderCounter', 'Headline', 'Body ID', 'Stance') )

   counter = 0
   for line in inputReader:
      newRow = []
      newRow.append(counter)
      newRow = newRow + line
      outputWriter.writerow( newRow )
      counter = counter + 1


def addBodyCounter(inputFile, outputFile):
   inputReader = csv.reader(inputFile)
   outputWriter = csv.writer(outputFile)
   firstValue = next(inputReader)
   if not firstValue == ['Body ID', 'articleBody']:
      raise ValueError("The input file's first row does not comform to the documented format")
   outputWriter.writerow( ('BodyCounter', 'Body ID', 'articleBody') )

   counter = 0
   for line in inputReader:
      newRow = []
      newRow.append(counter)
      newRow = newRow + line
      outputWriter.writerow( newRow )
      counter = counter + 1
