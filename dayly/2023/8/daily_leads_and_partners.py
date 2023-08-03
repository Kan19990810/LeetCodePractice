import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # groupby + agg
    # agg 两种使用方法 agg(name1=('name2', 'operate)) 新增一个新name
    # agg({'name': 'operate'}) 原name上进行操作
    df = daily_sales.groupby(['date_id', 'make_name'])
    df = df.agg({'lead_id': 'nunique', 'partner_id': 'nunique'})
    # df = df.agg(unique_leads=('lead_id','nunique'),unique_partners=('partner_id','nunique'))
    df = df.reset_index()
    df = df.rename(columns={'lead_id': 'unique_leads', 'partner_id': 'unique_partners'})
    # df = df[['date_id', 'make_name', 'unique_leads', 'unique_partners']]
    return df