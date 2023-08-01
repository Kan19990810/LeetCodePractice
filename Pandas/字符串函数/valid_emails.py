import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # 判断是否格式正确
    # 正则表达式 str.match
    return users[users['mail'].str.match(r'^[a-zA-Z][a-zA-Z0-9_.-]*\@leetcode\.com$')]