import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # 查询字符串是否包含 str.contain
    # \b 边界 空格？
    # return patients[patients['conditions'].str.contains(r'\bDIAB1', regex=True)]
    return patients[patients['conditions'].str.startswith('DIAB1') | patients['conditions'].str.contains(' DIAB1', regex=False)]  