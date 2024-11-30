import pandas as pd

mydict = {
    'val': 1,
    'qwe': 2,
    'asd': 3
}

df = pd.DataFrame(
    data=mydict.items(),
    columns=['str', 'int']
)

print(df)