import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = (accounts['income'] < 20000)
    low_count = low_salary.sum()

    average_salary = ((20000 <= accounts['income']) & (accounts['income'] <= 50000))
    average_count = average_salary.sum()

    high_salary = (accounts['income'] > 50000)
    high_count = high_salary.sum()

    df = pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary'], 'accounts_count': [low_count, average_count, high_count]})
    return df