import pandas as pd
from pandas import DataFrame


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
        'Wroclaw',
        'Bydgoszcz / Torun',
        'Lublin',
        'Gorzow Wielkopolski / Zielona Gora',
        'Lodz',
        'Krakow',
        'Warszawa'
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
    df = df.where(df['surface'] < 20000).dropna()
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
    cols = [col for col in df.columns if col != 'capital_cities'] + ['capital_cities']
    df = df[cols]
    print(df)

task_4()