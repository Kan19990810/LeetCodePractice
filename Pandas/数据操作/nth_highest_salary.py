import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # 排序 选取第N位
    df = employee[['salary']].drop_duplicates()
    if len(df) < N:
        return pd.DataFrame({'getNthHighestSalary(2)': [None]})
    # head 选取前 N 位， tail 选取后 N 位
    return df.sort_values('salary', ascending=False).head(N).tail(1)
