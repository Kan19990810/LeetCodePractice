import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # 不能对齐的两个表 拼接 merge() on 合并的列 how 以哪个表为基准
    employee_name_uni = pd.merge(employees, employee_uni, on='id', how='left')
    answer = employee_name_uni[['unique_id', 'name']]
    return answer