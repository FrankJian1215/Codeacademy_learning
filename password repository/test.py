import pandas as pd
import json

list = []
with open('password.txt', "r") as data:
    txt = data.readlines()
    for i in txt:
        list.append(i.replace('\n', '').split(' | '))
df = pd.DataFrame(list, columns=['platform', 'account', 'password'])
print(df)

print((df['platform'] == 'twitter') & (df['account'] == 'gmail'))

print(df.loc[df['platform'] == 'twitter','password'].item())
print(df.loc[df['platform'] == 'twitter', 'platform'].item() == 'twitter')

with open('password.json', 'r') as file:
    data = json.load(file) 
if 'peacefrank751215@gmail.com' in data:
    print('Yes!')
