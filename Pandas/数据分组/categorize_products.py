import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # 分组 groupby 重新整理 agg() 聚合操作 增加额外一列 nunique 不同的数目， unique 不同的单位集合
    df = activities.groupby("sell_date")
    stats = df.agg(num_sold=('product','nunique'),products=('product', lambda x: ','.join(sorted(set(x))))).reset_index()
    # 按日期进行排序
    stats.sort_values('sell_date', inplace=True)
    return stats