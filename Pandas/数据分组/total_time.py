import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    # groupby 按多个类别进行分群  reset_index() 将'event_day' 'emp_id' 索引互换
    employees = employees.groupby(['event_day', 'emp_id'])['total_time'].sum().reset_index()
    employees.rename({'event_day': 'day'}, axis=1, inplace=True)
    employees['day'] = employees['day'].astype(str)
    return employees