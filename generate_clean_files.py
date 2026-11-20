import pandas as pd


SAVE_PATH = '/Users/wsrdf/Documents/data-analysis-lab/Data'

REMOVE_REGIONS = [
    "Краснодарский край (с учетом ФТ «Сириус»)",
    "Российская Федерация без учета новых субъектов (с 01.01.2023)",
    "Архангельская область",
    # "Дальневосточный федеральный округ",
    # "Приволжский федеральный округ",
    # "Северо-Западный федеральный округ",
    # "Северо-Кавказский федеральный округ",
    "Сибирский федеральный округ",
    "Тюменская область",
    # "Уральский федеральный округ",
    # "Центральный федеральный округ",
    # "Южный федеральный округ",
    "Российская Федерация",
    "Астраханская область",
]

sheets = pd.read_excel('raw_x.xlsx', sheet_name=None, header=6, index_col=0) # make raw_data with Y in it

for name, df in sheets.items():
    
    if "x" in name.lower() and len(name) < 4:
        print(f"Processing sheet: {name}")
        df = df.drop(index=REMOVE_REGIONS, errors="ignore")
        df = df[~df.index.astype(str).str.contains('федеральный округ', case=False, na=False)]
        print(df.head())
        df = df.sort_index()
        print(df.shape)
        
        df.to_csv(f"{SAVE_PATH}/{name}.csv", index=True, header=True, encoding='utf-8')

