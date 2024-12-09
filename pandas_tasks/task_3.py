import pandas as pd
from pandas import DataFrame
import numpy as np


def load_data() -> DataFrame:
    regions = [
        'dolnoslaskie',
        'kujawsko-pomorskie',
        'lubelskie',
        'lubuskie',
        'tedzkie',
        'matopolskie',
        'mazowieckie',
    ]

    capital_cities = [
        'wroclaw',
        'bydgoszcz / Torun',
        'lublin',
        'gorzow Wielkopolski / Zielona Gora',
        'lodz',
        'krakow',
        'warszawa'
    ]

    surfaces = [
        19_946.70,
        17_971.34,
        25_122.46,
        13_987.93,
        18_218.95,
        15_182.79,
        35_558.47,
    ]

    population = [
        2904198,
        2086210,
        2139726,
        1018084,
        2493603,
        3372618,
        5349114,
    ]

    register_numbers = [
        2, 4, 6, 8, 10, 12, 14
    ]

    pd.set_option('display.max_columns', None)  # Show all columns
    pd.set_option('display.width', None)  # Disable line wrapping
    pd.set_option('display.max_colwidth', None)  # Disable truncation of column content

    return pd.DataFrame({
        'regions': regions,
        'register_numbers': register_numbers,
        'capital_cities': capital_cities,
        'surface': surfaces,
        'population': population

    })


def task_1():
    df = load_data()
    df = df.where(df['surface'] < 20_000).dropna()
    print(df)

def task_2():
    df = load_data()
    new_df = df.where(df['population'] > 2_000_000).dropna()
    print(new_df)

def task_3():
    df = load_data()
    df.loc[len(df)] = ['wielkopolskie', 30, 'Poznan', 29_826.50, 3_475_323]
    print(df)

def task_4():
    df = load_data()
    df = df.sort_values(by='population', ascending=False)
    print(df)

def task_5():
    df = load_data()
    cols = [col for col in df.columns if col != 'capital_cities'] + ['capital_cities']
    df = df[cols]
    print(df)

def task_6():
    df = load_data()
    df['capital_cities'] = df['capital_cities'].str.capitalize()
    print(df)    

def task_7():
    df = load_data()

    specific_regions = {}
    for i, row in df.iterrows():
        if (row['population'] / row['surface']) >= 140.0:
            specific_regions[row['regions']] = True
        else: 
            specific_regions[row['regions']] = False
    
    print(specific_regions)

def task_8():
    df = load_data()
    df = df[df['regions'] != 'lubuskie']
    print(df)

def task_9():
    df = load_data()
    described = df.describe(include=np.number)
    print(described)

task_9()