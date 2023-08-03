import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # 以 teacher 和 project_id 为群组 groupby 进行计数不同值 unique
    df = teacher.groupby(['teacher_id'])['subject_id'].nunique().reset_index()
    df = df.rename({'subject_id': 'cnt'}, axis=1)
    return df