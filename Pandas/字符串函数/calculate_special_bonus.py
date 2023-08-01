import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # 向量化 apply() 一次对整个或行应用操作 axis = 1 行处理
    # 首字母 .startswtih
    # employees['bonus'] 直接加一行
    employees['bonus'] = employees.apply(lambda x: x['salary'] if x['employee_id'] % 2 and not x['name'].startswith('M') else 0,
                                         axis=1)
    df = employees[['employee_id', 'bonus']].sort_values('employee_id')
    return df