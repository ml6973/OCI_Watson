import configuration.globalVars as globalVars
import json
import requests
import time

def getTones(inputFile, outputFile):
   globalVars.init()
   my_headers = {"Content-Type": 'text/plain'}
   auth = requests.auth.HTTPBasicAuth(globalVars.userName, globalVars.password)
   for line in inputFile:
      r = requests.post(globalVars.url, data=line, headers=my_headers, auth=auth)
      while r.status_code == requests.codes.too_many:
         time.sleep(60)
         r = requests.post(globalVars.url, data=line, headers=my_headers, auth=auth)
      if not r.status_code == requests.codes.ok:
         print "API Request Error"
         print r
         print r.text
         return
      json_results = r.json()
      for tone in json_results['document_tone']['tone_categories'][0]['tones'][:-1]:
         outputFile.write(str(tone['score']) + " ")
      outputFile.write(str(json_results['document_tone']['tone_categories'][0]['tones'][-1]['score']) + "\n")
