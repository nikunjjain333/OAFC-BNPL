import pandas as pd
import numpy as np

data_text1 = pd.read_csv("data2.csv", )
df1 = data_text1.replace(['-0-'], np.nan, regex=True)
df1.columns = ['Id', 'Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6', 'Column7', 'Column8', 'Column9',
               'Column10', 'Column11']
# print(df1.head(3))

data_text2 = pd.read_csv("data3.csv", )
df2 = data_text2.replace(['-0-'], np.nan, regex=True)
df2.columns = ['Id', 'Column1', 'Column2', 'Column3', 'Column4']
# print(df2.head(3))

data_text3 = pd.read_csv("data4.csv", )
df3 = data_text3.replace(['-0-'], np.nan, regex=True)
df3.columns = ['Id', 'Column1', 'Column2', 'Column3', 'Column4', 'Column5']
# print(df3.head(3))

output1 = pd.merge(df1, df2, on='Id', how='inner')
output2 = pd.merge(output1, df3, on='Id', how='inner')
output2.to_csv('result.csv', index=False)
output2.to_csv('filterresult.csv', index=False)
# print(output2.head(3))
print(output2.columns)


# data after filtering

filter = pd.read_csv("filterresult.csv")
for col in filter.columns:
    nan_percentage = (filter[col].isnull().sum() / filter[col].size) * 100
    if not nan_percentage >= 80:
        print(nan_percentage)
        filter.dropna(axis=1)
print(filter.columns)


id = filter['Id']
name = filter['Column1_x']
dob = filter['Column11']
loc = filter['Column2']+', '+filter['Column3']+', '+filter['Column4']

data = {'Id':id, 'Name': name,'DOB':dob,"Location":loc}
df = pd.DataFrame(data)
df.to_csv('finaldata.csv',index=False)