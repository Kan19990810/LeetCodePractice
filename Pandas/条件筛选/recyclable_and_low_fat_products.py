import pandas as pd

def recyclable_and_low_fat_products(products: pd.DataFrame) -> pd.DataFrame:
    # 行过滤 
    df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return df[['product_id']]