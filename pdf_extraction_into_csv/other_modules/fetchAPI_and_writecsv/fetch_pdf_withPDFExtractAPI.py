from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType

import logging
import shutil
import json
import zipfile
import os.path

def fetch_Pdf_extractAPI(cur_pdf):
    zip_file = "/zipFilesfromAPI/ExtractFromPDF.zip"
    zip_file_name1="./zipFilesfromAPI/ExtractFromPDF.zip"
    if os.path.isfile(os.getcwd()+zip_file):
        print(os.getcwd()+zip_file,"curent dire")
        # print(" -------  ",zip_file_name1)
        os.remove(os.getcwd()+zip_file)

    input_pdf = cur_pdf

    try:
    #Initial setup, create credentials instance.
        credentials = Credentials.service_account_credentials_builder()\
            .from_file("./pdfservices-api-credentials.json") \
            .build()

        #Create an ExecutionContext using credentials and create a new operation instance.
        execution_context = ExecutionContext.create(credentials)
        extract_pdf_operation = ExtractPDFOperation.create_new()

        #Set operation input from a source file.
        source = FileRef.create_from_local_file(input_pdf)
        extract_pdf_operation.set_input(source)

        #Build ExtractPDF options and set them into the operation
        extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
            .with_element_to_extract(ExtractElementType.TEXT) \
            .build()
        extract_pdf_operation.set_options(extract_pdf_options)

        #Execute the operation.
        result: FileRef = extract_pdf_operation.execute(execution_context)

        #Save the result to the specified location.
        # result.save_as(zip_file)
        location_zipfile=result._file_path
        print(os.getcwd()+zip_file ,"curloc-------")
        des_loc=os.getcwd()+zip_file
        shutil.move(location_zipfile,des_loc)

        print("Successfully extracted information ")

        archive = zipfile.ZipFile(os.getcwd()+zip_file, 'r')
        jsonentry = archive.open('structuredData.json')
        jsondata = jsonentry.read()
        data = json.loads(jsondata)
        # print(data)
        return data

    except (ServiceApiException, ServiceUsageException, SdkException):
        logging.exception("Exception encountered while executing operation")