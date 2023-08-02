import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # 合并表 merge(left_on 左对齐， left_on 右对齐， how 放置哪边)
    df = employee.merge(department, left_on='departmentId', right_on='id', how='left')
    df.rename(columns={'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'}, inplace=True)

    # 按部门进行分群 groupby('')， 选择每个群中工资最高的员工 .transform('max')
    max_salary = df.groupby('Department')['Salary'].transform('max')
    df = df[df['Salary'] == max_salary]
    return df[['Department', 'Employee', 'Salary']]