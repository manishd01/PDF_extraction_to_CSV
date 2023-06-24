import os
import csv
# funciton used to get that one liner info  from pdf and push it in csv file
def push_in_csvF(required_info):
    location_csv=os.getcwd()+"/OutputCSVFile/output.csv"
    with open(location_csv,'a',newline='') as file:
        writer_obj=csv.writer(file)
        writer_obj.writerow(required_info)
        file.close() 
    
    print("written success!")