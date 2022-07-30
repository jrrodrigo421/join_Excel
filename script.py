import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arquivo_excel_1 = 'Book1.xlsx'
arquivo_excel_2 = 'Book2.xlsx'


df_dia_1 = pd.read_excel(arquivo_excel_1,sheet_name='Sheet1')
df_dia_2 = pd.read_excel(arquivo_excel_1,sheet_name='Sheet2')
df_dia_3 = pd.read_excel(arquivo_excel_2,sheet_name='Sheet1')
df_dia_4 = pd.read_excel(arquivo_excel_2,sheet_name='Sheet2')



# print(df_dia_1)
# print(df_dia_2)
# print(df_dia_3)

# df_consolidado = pd.concat([df_dia_1, df_dia_2, df_dia_3,df_dia_4])
df_header = pd.concat([df_dia_1,df_dia_3])
df_line = pd.concat([df_dia_2,df_dia_3])
df_teste = pd.concat([df_dia_1,df_dia_4] + [df_dia_2,df_dia_4])
# df_teste = pd.concat([df_header, df_line])
# def_teste = pd.read_excel(arquivo_excel_3)
# print(df_consolidado)

# df_header.to_excel('HEADER.xlsx', sheet_name='Pre-PO Header')
# df_line.to_excel('LINE.xlsx', sheet_name='Pre-PO Line')


df_teste.to_excel('Final.xlsx')


