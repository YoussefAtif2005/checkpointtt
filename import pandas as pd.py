import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


df=pd.DataFrame(exam_data, index=l)

#1
print(df.head(3))
#2
print("##################################################################################")
data=df.dropna()
#3
print("##################################################################################")
print(data[['name','score']])
#4
print("######################################################################################")
new_row =pd.DataFrame({'name': 'Suresh','score': 15.5,'attempts': 1,'qualify': 'yes'}, index=['k'])
    
  
data = pd.concat([data, new_row])
print(data)
#5
print("#####################################################################################################")
print(data.drop('attempts', axis=1))
data=data.drop('attempts', axis=1)
#6
print('####################################################################################################"')
data['Success'] = data['score'].apply(lambda x: 1 if x > 10 else 0)
print(data)
#7
data.to_csv('scores.csv')
