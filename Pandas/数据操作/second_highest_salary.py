import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    dp = employee[['salary']].drop_duplicates()
    if len(dp) < 2:
        # {'': []}
        return pd.DataFrame({'SecondHighestSalary': [None]})
    # sort_values('', ascending=)
    # head() tail()
    # rename(columns={'': ''})
    return dp.sort_values('salary', ascending=False).head(2).tail(1).rename(columns={'salary':'SecondHighestSalary'})