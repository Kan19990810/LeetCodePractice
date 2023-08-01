import pandas as pd

def big_countries(World: pd.DataFrame) -> pd.DataFrame:
    # 行过滤， 选取符合条件的行
    df = World[(World['area'] >= 3000000) | (World['population'] >= 25000000)]
    return df[['name', 'population', 'area']]