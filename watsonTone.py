import configuration.globalVars as globalVars
import csv
import json
import requests
import time

def getHeaderTones(inputFile, outputFile):
   inputReader = csv.reader(inputFile)
   outputWriter = csv.writer(outputFile)
   firstValue = next(inputReader)
   if not firstValue == ['Headline', 'Body ID', 'Stance']:
      raise ValueError("The input file's first row does not comform to the documented format")
   outputWriter.writerow( ('Body ID', 'anger', 'disgust', 'fear', 'joy', 'sadness') )

   globalVars.init()
   my_headers = {"Content-Type": 'text/plain'}
   auth = requests.auth.HTTPBasicAuth(globalVars.userName, globalVars.password)
   for line in inputReader:
      r = requests.post(globalVars.url, data=line[0], headers=my_headers, auth=auth)
      while r.status_code == requests.codes.too_many:
         time.sleep(60)
         r = requests.post(globalVars.url, data=line[0], headers=my_headers, auth=auth)
      if not r.status_code == requests.codes.ok:
         print "API Request Error"
         print r
         print r.text
         return
      json_results = r.json()
      newRow = []
      newRow.append(line[1])
      for tone in json_results['document_tone']['tone_categories'][0]['tones']:
         newRow.append(tone['score'])
      outputWriter.writerow( newRow )


def getBodyTones(inputFile, outputFile):
   inputReader = csv.reader(inputFile)
   outputWriter = csv.writer(outputFile)
   firstValue = next(inputReader)
   if not firstValue == ['Body ID', 'articleBody']:
      raise ValueError("The input file's first row does not comform to the documented format")
   outputWriter.writerow( ('Body ID', 'anger', 'disgust', 'fear', 'joy', 'sadness') )

   globalVars.init()
   my_headers = {"Content-Type": 'text/plain'}
   auth = requests.auth.HTTPBasicAuth(globalVars.userName, globalVars.password)
   for line in inputReader:
      r = requests.post(globalVars.url, data=line[1], headers=my_headers, auth=auth)
      while r.status_code == requests.codes.too_many:
         time.sleep(60)
         r = requests.post(globalVars.url, data=line[1], headers=my_headers, auth=auth)
      if not r.status_code == requests.codes.ok:
         print "API Request Error"
         print r
         print r.text
         return
      json_results = r.json()
      newRow = []
      newRow.append(line[0])
      for tone in json_results['document_tone']['tone_categories'][0]['tones']:
         newRow.append(tone['score'])
      outputWriter.writerow( newRow )
