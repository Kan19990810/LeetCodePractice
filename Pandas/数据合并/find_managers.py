import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # merge(how='inner') 只会选择两个表都匹配的行
    groups = employee.groupby('managerId').size().reset_index(name='count')
    groups = groups[groups['count'] >= 5]
    answer = pd.merge(employee, groups, left_on='id', right_on='managerId', how='inner')
    return answer[['name']]