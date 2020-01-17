
import pandas as pd


df1 = pd.read_excel("C:/Users/wisdom/desktop/data.csv")
df2 = pd.read_excel("C:/Users/wisdom/desktop/data.csv")

df=pd.concat([df1,df2])
print(df)

## TypeError: '<' not supported between instances of 'str' and 'float'
#Delete row with dummy value
df = df.dropna(how='any',axis=0)
print(df)