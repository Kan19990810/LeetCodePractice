import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # .str 对于字符串的访问器 str[1:] str.lower()
    users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    return users.sort_values('user_id')