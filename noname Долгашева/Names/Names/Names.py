import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecs




columns = ['ID','FIO' , 'BD', 'Tel']


path = 'C:\\Users\\asus\\source\\repos\\практика\\Names\\RedWhite_test.txt' 
frame = pd.read_csv(path, sep='\t', dtype=str, error_bad_lines=False)

#frame=frame.drop(np.where(frame['Tel']=='NULL'))
frame.dropna(subset=['TelKont'], inplace=True)
print('Записываю')

frame.to_csv('C:\\Users\\asus\\source\\repos\\практика\\Names\\New_file_test.txt')


#print(frame) df = df.drop(np.where(df['STP'] == 1005092)[0])
print('Готово')