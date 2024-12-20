import pandas as pd
import random
import numpy as np

def generate_data_frame(number_of_columns: int) -> pd.DataFrame:
    number_of_columns = abs(number_of_columns)
    if number_of_columns > 26:
        number_of_columns = 26

    columns = []

    for i in range(65, 65+number_of_columns):
        columns.append(chr(i))

    data = {}
    for col in columns:
        col_data = []
        for j in range(0, 32):
            col_data.append(2**j)
        data[col] = col_data
    df = pd.DataFrame(data)
    
    df = pd.DataFrame(data).astype('Int64')  # Use 'Int64' for nullable integer support

    for col in df.columns:
        index = random.choice(df.index)
        df.at[index, col] = np.nan
            
    print(df)
    return df

        
def get_column_average_value(column: pd.Series) -> int:
    sum = column.sum
    return sum // len(column)


df = generate_data_frame(25)


for col in df.columns:
    for index, val in df[col]:
        