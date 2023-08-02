import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # .sum()    round() 数值四舍五入
    is_valid = (delivery['order_date'] == delivery['customer_pref_delivery_date'])
    valid_count = is_valid.sum()
    total_count = len(delivery)
    percentage = round(100 * valid_count / total_count, 2)
    df = pd.DataFrame({'immediate_percentage': [percentage]})
    return df