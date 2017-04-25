import csv

def mergeTables(headerFile, bodyFile, outputFile):
   headerReader = csv.reader(headerFile)
   bodyReader = csv.reader(bodyFile)
   outputWriter = csv.writer(outputFile)

   firstValue = next(headerReader)
   if not firstValue == ['HeaderCounter', 'Body ID', 'anger', 'disgust', 'fear', 'joy', 'sadness', 'Stance']:
      raise ValueError("The header input file's first row does not comform to the documented format")

   firstValue = next(bodyReader)
   if not firstValue == ['BodyCounter', 'Body ID', 'anger', 'disgust', 'fear', 'joy', 'sadness']:
      raise ValueError("The body input file's first row does not comform to the documented format")

   outputWriter.writerow( ('Counter', 'Body ID', 'headerAnger', 'headerDisgust', 'headerFear', 'headerJoy', 'headerSadness', 'Stance', 'bodyAnger', 'bodyDisgust', 'bodyFear', 'bodyJoy', 'bodySadness') )
    
   for line in headerReader:
      bodyID = line[1]
      for bodyLine in bodyReader:
         if bodyID == bodyLine[1]:
            newRow = []
            newRow.append(line[0])
            newRow = newRow + line[1:8]
            newRow = newRow + bodyLine[2:7]
            outputWriter.writerow( newRow )
            break
      bodyFile.seek(0)
      next(bodyReader)
