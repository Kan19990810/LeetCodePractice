import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # 对字符串进行判断 行过滤
    # str.len() 检索字符串元素长度
    # is_valid 对应长度大于 15 的行
    is_valid = tweets['content'].str.len() > 15
    # [] 行筛选
    df = tweets[is_valid]
    # [[]] 列筛选
    return df[['tweet_id']]