from other_modules import getting_pdfs, writing_col_names, extract_from_curpdf

if __name__ =="__main__":
    #Code flow starts from here
    # getting_pdfsF() is used to get all pdfs from that directory in pdf_list list
    pdf_list=getting_pdfs.getting_pdfsF()
    
    #considering all pdfs have structure but different data
    # writing_col_names() function is used to adding column names inCSV file
    writing_col_names.writing_col_names()

    # funciton to extract data by itrating over all pdfs
    extract_from_curpdf.extract_from_curPDF(pdf_list)

    # extraction and writing in pdf has beeen done :)


    


