import pandas as pd

# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:

    # 相同值的email进行处理， groupby  查询最小值所在的行 .transform('min')
    min_id = person.groupby('email')['id'].transform('min')
    # 应该清除的数据结构
    removed_person = person[person['id'] != min_id]
    # drop(removed_person.index) 根据索引清除 drop 直接修改
    person.drop(removed_person.index, inplace=True)
    
    return
