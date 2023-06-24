import os
import glob
def getting_pdfsF():
    # iterate over all pdf file
    # if first pdf add attributes/columns in the CSV file -> output.csv
    # for rest of rows add tuples only
    pdf_list=[]
    pdf_direct_name="/TestDataSet"
    csv_direct_name='./OutputCSVFile.csv'
    # each time create new output
    if os.path.isfile(csv_direct_name):
        os.remove(csv_direct_name)

    cur_direct_name=os.getcwd()+pdf_direct_name
    print(cur_direct_name)

    # iterating over all PDFs in that directory
    for root, dirs, files in os.walk(cur_direct_name):
        pdf_list+=glob.glob(os.path.join(root,'*.pdf'))

    return pdf_list