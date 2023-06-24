from other_modules.fetchAPI_and_writecsv import push_in_csv, fetch_pdf_withPDFExtractAPI
# from fetchAPI_and_writecsv import fetch_pdf_withPDFExtractAPI
def fetch_info_from_json(line):

    ansin=[]
    for i in line["elements"]:
        for j in i:
            if(j=="Text"):
                ansin.append(i[j])
                print(i[j])
    
    return ansin

def futhur_fetching(required_info):
    # making the info in string form for easy manipulation --
    instr_from =  ' * '.join(required_info)

    # print(instr_from,"ssssssssssssssssssssssssssssssssssssssssss-----")
    finalans=[None]*19
    
    i=0
    finalans[0]=required_info[1].split(",", 1)[1].strip()
    finalans[1]=required_info[2]
    finalans[2]=required_info[8]
    finalans[3]=required_info[0]
    finalans[4]=required_info[1].split(",")[0].strip()
    finalans[5]=required_info[3]
    
    #  to get next word that is after *
    def get_nextword(i,st):
        t=i
        new_word=""
        while(t<len(st) and st[t]!='*'):
            new_word+=st[t]
            print(new_word,"tt")
            t+=1
        new_word.strip()
        t+=1 # to skip that '^'
        return t,new_word
    
    i1=instr_from.index("BILL TO")
    i2=instr_from.index("DETAILS")
    st=instr_from[i1:i2]
    t=0
    t,new_Wrd=get_nextword(t,st) #removing first word:
    
    t,new_Wrd=get_nextword(t,st) #name
    finalans[9]=new_Wrd

    t,new_Wrd=get_nextword(t,st) #email
    finalans[8]=new_Wrd
    t,new_Wrd=get_nextword(t,st) #ph num
    finalans[10]=new_Wrd
    t,new_Wrd=get_nextword(t,st) #addr1
    finalans[6]=new_Wrd
   
    t,new_Wrd=get_nextword(t,st) #addr2
    finalans[7]=new_Wrd
    
    i1=instr_from.index("AMOUNT")
    # i2=instr_from.index("DETAILS")
    st=instr_from[i1:]
    t,new_Wrd=get_nextword(t,st)
    t,new_Wrd=get_nextword(t,st)
    finalans[11]=new_Wrd
    t,new_Wrd=get_nextword(t,st)
    finalans[12]=new_Wrd
    t,new_Wrd=get_nextword(t,st)
    finalans[13]=new_Wrd

    #details
    i1=instr_from.index("DETAILS")
    st=instr_from[i1:]
    t,new_Wrd=get_nextword(t,st)
    t,new_Wrd=get_nextword(t,st)
    finalans[14]=new_Wrd

    #duedata
    i1=instr_from.index("Due date:")
    st=instr_from[i1:]
    t,new_Wrd=get_nextword(t,st)
    t,new_Wrd=get_nextword(t,st)
    finalans[15]=new_Wrd

    #issue date
    i1=instr_from.index("Issue date")
    st=instr_from[i1:]
    t,new_Wrd=get_nextword(t,st)
    t,new_Wrd=get_nextword(t,st)
    finalans[16]=new_Wrd

     #invoice numebr
    i1=instr_from.index("Invoice#")
    st=instr_from[i1:]
    t,new_Wrd=get_nextword(t,st)
    t,new_Wrd=get_nextword(t,st)
    finalans[17]=new_Wrd

     #tax
    i1=instr_from.index("Tax %")
    st=instr_from[i1:]
    t,new_Wrd=get_nextword(t,st)
    t,new_Wrd=get_nextword(t,st)
    finalans[18]=new_Wrd

    print(finalans,"88888") 
    return finalans

# main funciton of this file ------------------------------
def extract_from_curPDF(p):
    # pass
    dict_ans={}
    for i in p:
        #  getting pdf full content and using Adobe PDF extract API
        line=fetch_pdf_withPDFExtractAPI.fetch_Pdf_extractAPI(i)

        # fetch_info_from_json () func used to getting all titles and text in the pdf 
        required_info=fetch_info_from_json(line)

        # futhur_fetching() func is used to get informatoion that is being pushed in CSv file
        required_info_19element=futhur_fetching(required_info)

        push_in_csv.push_in_csvF(required_info_19element)