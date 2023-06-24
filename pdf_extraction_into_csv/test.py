import pdfplumber

def get_element_dimensions(pdf_path):
    dimensions = []
    with pdfplumber.open(pdf_path) as pdf:
        num_pages = len(pdf.pages)

        for page_num in range(num_pages):
            page = pdf.pages[page_num]
            elements = page.extract_text().strip().split('\n')
            for element in elements:
                x, y = 0, 0  # Set initial coordinates to 0
                dimensions.append({'text': element, 'x': x, 'y': y})

    return dimensions

pdf_path = '/media/dogra02/DoGra_2/papyrus nabulae/InvoicesData/TestDataSet/output1.pdf'
element_dimensions = get_element_dimensions(pdf_path)
for element in element_dimensions:
    print(element)

print(len(element_dimensions))







# data = "<NearBy Electronics  3741 Glory Road, Jamestown,  Tennessee, USA  38556 Invoice# NL57EPAS7793742478  Issue date  12-05-2023  NearBy Electronics  We are here to serve you better. Reach out to us in case of any concern or feedbacks.  BILL TO  Willis Koelpin  Willis_Koelpin4@yahoo.co  m  783-402-5895  353 Cara Shoals  Suchitlán  DETAILS  minim velit velit fugiat culpa  deserunt ex aliquip cillum est  aliqua ex amet amet  PAYMENT  Due date: 08-07-2023  $22337.7  ITEM  QTY  RATE  AMOUNT  Rustic Rubber Gloves  102 29 $2958  Fantastic Granite Salad  39 27 $1053  Small Fresh Salad  95 69 $6555  Fantastic Metal Chips  67 49 $3283  Refined Cotton Pants  79 72 $5688  Ergonomic Concrete Towels  35 22 $770  Subtotal  $20307  Tax %  10 Total Due  $22337.7 >"

# # Remove unnecessary characters and split the string
# data = data.replace("<", "").replace(">", "").replace("$", "").replace("Invoice# ", "Invoice#").strip()
# data = data.replace("  ", " ").replace("\t", " ")
# data_list = data.split(" ")

# # Extract the required elements
# location = data_list[0]
# address = data_list[1] + ", " + data_list[2]
# details = " ".join(data_list[15:18])
# customer_name = data_list[12]
# contact = data_list[13]
# email = data_list[11]
# phone = data_list[14]
# issue_date = data_list[7]
# payment_due_date = data_list[9]
# invoice_number = data_list[8]
# tax_percentage = data_list[-3]
# total_due = data_list[-1]

# # Create the final list of strings with 19 elements
# output = [
#     location,
#     address,
#     details,
#     customer_name,
#     contact,
#     email,
#     phone,
#     issue_date,
#     payment_due_date,
#     invoice_number,
#     tax_percentage,
#     total_due,
#     "",  # Empty placeholder for the first item name (to align with the desired format)
#     *data_list[19:-3],  # Items and their details
#     "",  # Empty placeholder for the last column (to align with the desired format)
# ]

# print(output)


