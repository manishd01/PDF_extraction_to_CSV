import csv
def writing_col_names():
    # adding fixed column names:
    cols_name=['Bussiness__City','Bussiness__Country','Bussiness__Description','Bussiness__Name',
            'Bussiness__StreetAddress','Bussiness__Zipcode'	,'Customer__Address__line1','Customer__Address__line2'
            ,'Customer__Email','Customer__Name','Customer__PhoneNumber','Invoice__BillDetails__Name'	
            ,'Invoice__BillDetails__Quantity','Invoice__BillDetails__Rate','Invoice__Description'
            ,'Invoice__DueDate','Invoice__IssueDate','Invoice__Number','Invoice__Tax'   
        ]
    
    with open('./OutputCSVFile/output.csv','w',newline='\n') as file:
        # adding column names using writerheader() function
        writer_obj=csv.DictWriter(file,fieldnames=cols_name)
        writer_obj.writeheader()
    
    print("written colname done:")