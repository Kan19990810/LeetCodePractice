import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # merge(how='cross') 交叉合并
    # fillna(0)。astype(int) 用0 填充 null
    groups = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    all_id_subjects = pd.merge(students, subjects, how='cross')
    id_subjects_count = pd.merge(all_id_subjects, groups, on=['student_id', 'subject_name'], how='left')
    id_subjects_count['attended_exams'] = id_subjects_count['attended_exams'].fillna(0).astype(int)
    id_subjects_count.sort_values(['student_id', 'subject_name'], inplace=True)
    return id_subjects_count[['student_id', 'student_name', 'subject_name', 'attended_exams']]