import pandas as pd


SAVE_PATH = '/Users/wsrdf/Documents/data-analysis-lab/Data'

REMOVE_REGIONS = [
    "Краснодарский край (с учетом ФТ «Сириус»)",
    "Российская Федерация без учета новых субъектов (с 01.01.2023)",
    "Архангельская область",
    "Тюменская область",
    "Российская Федерация",
    "Астраханская область",
    "ГУ МВД России по г.Санкт-Петербургу и Ленинградской области",
    "Архангельская область (с а/о )",
    "Тюменская область (с а/о)",
]

sheets = pd.read_excel('raw_x.xlsx', sheet_name=None, header=6, index_col=0) # make raw_data with Y in it

def check_sheet(df: pd.DataFrame, name: str):
    print(f"Df {name} - Shape: {df.shape}")

for name, df in sheets.items():
    
    if "x" in name.lower() and len(name) < 4:
        # print(f"Processing sheet: {name}")
        
        # clear unwanted regions
        df = df.drop(index=REMOVE_REGIONS, errors="ignore")
        df = df[~df.index.astype(str).str.contains('федеральный округ', case=False, na=False)]
        df = df.sort_index()
        
        # check df
        check_sheet(df, name)
    
        df.to_csv(f"{SAVE_PATH}/{name}.csv", index=True, header=True, encoding='utf-8')

