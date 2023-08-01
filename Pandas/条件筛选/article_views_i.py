import pandas as pd

def article_views_i(views: pd.DataFrame) -> pd.DataFrame:
    # 筛选表中列相同的行
    df = views[views['author_id'] == views['viewer_id']]
    # 去掉重复的行 drop_duplicates subset 判断的值 inplace 覆盖
    df.drop_duplicates(subset=['author_id'], inplace=True)
    df = df[['author_id']].rename(columns={'author_id': 'id'})
    # 排序 sort_values by 判断的值
    df.sort_values(by=['id'],inplace=True)
    return df