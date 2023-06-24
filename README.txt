
project structure:
-pdf_extraction_into_csv contains all the API credential and main code folder with same name: pdf_extraction_into_csv

inside -pdf_extraction_into_csv directory:
- maincode.py -> file where the code flow starts , we have to run this file to run our project
- other_modules: container all the nescessary function in the form of different modules and a folder
    - fetchAPI_and_writecsv=> contais the files contains code for fetching API  and writing record into CSV file that is inside 
      output CSV file
- OutputCSVFile contains the resultant CSV files:
      - output: updating simultaneously when code is running
      - fullExtractedData file which is used to example template howwill the fetching happen
- TestDataSet -> contains the sample pdf which are needed to be extracted data from.
- zipFilesfromAPI -> contains the reponse ZIP from called API reponse, from which there is JSON to whoch we have to extracted             data from, and it simultaneously updating when code running.
- test.py and test.txt -> for checking working of any library/functions for testing , (not relevant to project)
- json file and privatekey : API credentials files consist password and keys.

modules need to project running:
import os
import glob
import csv
import logging
import shutil
import json
import zipfile
import os.path

The downloaded zip file contains your private key, credentials and personalized code samples. Please store your private key securely, since Adobe does not retain a copy of it. You can replace with your own public key on I/O Console.
