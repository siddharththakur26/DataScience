
'''
GIVEN SCRIPT COLLECTS THE DATA FROM THE URLs. EXTRACT THE THOSE FILES AND STORE IT IN THE TXT FILE FORMAT
'''
import script_data_extraction

'''
GIVEN SCRIPT CREATES THE JSON FORMAT DICTIONARY OF POSITIVE, NEGATIVE, UNCERTAIN AND CONSTRAINING WORD
'''
import script_word_dictionary

'''
IMPORTING FUNCTIONS TO CALCULATE 14 OUTPUT VARIABLES AND ONE ADDITIONL VARIABLE OF CALCULATING THE
CONSTRAINING WORDS IN WHOLE REPORT
'''
from script_sentimental_analysis import analyse_text_sentiments,calculate_constrain_words_whole_report
import xlsxwriter 
import pandas as pd
flag = True
i=1
df = pd.read_excel('cik_list.xlsx')
k=0
output_variables=[]
output=[]
'''
ITERATE OVER EVERY FILE AND CALCULATE THE OUPUT VARIABLES
'''
while(flag == True):    
    try:
        f = open("sec_file_mda_{}.txt".format(i),'r')
        string = f.read()
        output_variables = [df['CIK'][k],df['CONAME'][k],df['FYRMO'][k],df['FDATE'][k],df['FORM'][k],df['SECFNAME'][k]]
        output_variables = output_variables + analyse_text_sentiments(string)
        
        f = open("sec_file_qqdmr_{}.txt".format(i),'r')
        string = f.read()
        output_variables = output_variables + analyse_text_sentiments(string)
        
        f = open("sec_file_rf_{}.txt".format(i),'r')
        string = f.read()
        output_variables = output_variables + analyse_text_sentiments(string) +[calculate_constrain_words_whole_report(string)]
        
        
        
        f = open("sec_file_{}.txt".format(i),'r')
        string = f.read().lower()
        # STORE OUTPUT VARIABLE IN THE LIST
        output.append(output_variables)
        
        k+=1
    except Exception as ex:
        #print(ex)
        flag = False
    print("sec_file_{} is processed".format(i))
    i+=1
    

 # WORKBOOK IS INITIATED 
workbook = xlsxwriter.Workbook('Output Data.xlsx') 
worksheet = workbook.add_worksheet() 
  

# EXCEL COLUMNS ARE DEFINED
worksheet.write("A1",'CIK')
worksheet.write('B1','CONAME')
worksheet.write('C1','FYRMO')
worksheet.write('D1','DATE')
worksheet.write('E1','FORM')
worksheet.write('F1','SECFNAME')
worksheet.write('G1','mda_positive_score')
worksheet.write('H1','mda_negative_score')
worksheet.write('I1','mda_polarity_score')
worksheet.write('J1','mda_average_sentence_length')
worksheet.write('K1','mda_percentage_of_complex_words')
worksheet.write('L1','mda_fog_index')
worksheet.write('M1','mda_complex_word_count')
worksheet.write('N1','mda_word_count')
worksheet.write('O1','mda_uncertainty_score')
worksheet.write('P1','mda_constraining_score')
worksheet.write('Q1','mda_positive_word_propotion')
worksheet.write('R1','mda_negative_word_propotion')
worksheet.write('S1','mda_uncertainty_word_propotion')
worksheet.write('T1','mda_constraining_word_propotion')
worksheet.write('U1','qqdmr_positive_score')
worksheet.write('V1','qqdmr_negative_score')
worksheet.write('W1','qqdmr_polarity_score')
worksheet.write('X1','qqdmr_average_sentence_length')
worksheet.write('Y1','qqdmr_percentage_of_complex_words')
worksheet.write('Z1','qqdmr_fog_index')
worksheet.write('AA1','qqdmr_complex_wordount')
worksheet.write('AB1','qqdmr_word_Count')
worksheet.write('AC1','qqdmr_uncertainty_score')
worksheet.write('AD1','qqdmr_constraining_score')
worksheet.write('AE1','qqdmr_positive_word_proption')
worksheet.write('AF1','qqdmr_negative_word_propotion')
worksheet.write('AG1','qqdmr_uncertainty_word_propotion')
worksheet.write('AH1','qqdmr_constraining_word_propotion')
worksheet.write('AI1','rf_positive_score')
worksheet.write('AJ1','rf_negative_score')
worksheet.write('AK1','rf_polarity_score')
worksheet.write('AL1','rf_average_sentence_length')
worksheet.write('AM1','rf_percentage_of_complex_words')
worksheet.write('AN1','rf_fog_index')
worksheet.write('AO1','rf_complex_word_count')
worksheet.write('AP1','rf_word_count')
worksheet.write('AQ1','rf_uncertainty_score')
worksheet.write('AR1','rf_constraining_score')
worksheet.write('AS1','rf_positive_word_propotion')
worksheet.write('AT1','rf_negative_word_propotion')
worksheet.write('AU1','rf_uncertainty_word_propotion')
worksheet.write('AV1','rf_constraining_word_propotion')
worksheet.write('AW1', 'constraining_words_whole_report')
row=0  
for variable in output :
    column = 0        
    for value in variable:
        worksheet.write(row+1, column, value)
        column+=1 
    row +=1      
workbook.close() 


# DELETING FILES
'''
import os
for i in range(1,153):
    #os.remove("sec_file_{}.txt".format(i))
    #os.remove("sec_file_mda_{}.txt".format(i))
    #os.remove("sec_file_qqdmr_{}.txt".format(i))
    #os.remove("sec_file_rf_{}.txt".format(i))

'''

# SEQUENTIAL ORDER OF DISPLAYING THE OUTPUT VARIABLES (FOR REFERENCE)
'''
1.	mda_positive_score
2.	mda_negative_score
3.	mda_polarity_score
4.	mda_average_sentence_length
5.	mda_percentage_of_complex_words
6.	mda_fog_index
7.	mda_complex_word_count
8.	mda_word_count
9.	mda_uncertainty_score
10.	mda_constraining_score
11.	mda_positive_word_proportion
12.	mda_negative_word_proportion
13.	mda_uncertainty_word_proportion
14.	mda_constraining_word_proportion
'''