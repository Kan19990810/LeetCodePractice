import pandas as pd

def customers_who_never_order(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 两个表的排除条件过滤
    # 选择 order中‘id' 不存在的行
    # isin判断两个表的关系进行筛选
    df = customers[~customers['id'].isin(orders['customerId'])]
    
    # 只包含name的数据框架
    # name 重命名为 Customers
    # rename(columns=)
    return df[['name']].rename(columns={'name':'Customers'})