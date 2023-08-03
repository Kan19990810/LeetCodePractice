import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # 分组中行数最多的， size  sort_value
    df = orders.groupby('customer_number').size().reset_index(name='count')
    df = df.sort_values('count',ascending=False).head(1)
    df = df[['customer_number']]
    return df