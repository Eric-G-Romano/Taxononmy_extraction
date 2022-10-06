# import libaries
import PyPDF2 as pdf
import pandas as pd
import re 

pathfile = float(input("Input file path of the Taxonomy document"))

def taxonomy_extractor(pdf_file):
    opener = open(pdf_file, 'rb')
    reader = pdf.PdfFileReader(opener)
    
    text = ''
    for page in reader.pages:
        text += page.extractText()
        
    sentence_list = re.split('\n', text)
    
    taxonomy_list = []
    for i in sentence_list:
        if i.endswith('X'):
            taxonomy_list.append(i)
    
    specialization_list = []
    specialization_code_list = []
    for x in taxonomy_list:
        specialization_list.append(" ".join(x.split(' ')[:-1]))
        specialization_code_list.append(x.split(' ')[-1])
    
    taxonomy_dataframe = pd.DataFrame({'Specialization': specialization_list,
                                       'Code': specialization_code_list})
    
    return taxonomy_dataframe

taxonomy_extractor(pathfile).to_excel("output.xlsx", sheet_name='Sheet_name_1')

input("Check if excel file was created with the title output, if so press any key to exit")
