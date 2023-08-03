import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # order_company = pd.merge(orders, company, on='com_id', how='left')
    # order_company_salesperson = pd.merge(order_company, sales_person, on='sales_id', how='left')
    # print(order_company_salesperson)
    # #  order_company_salesperson = order_company_salesperson[order_company_salesperson['name'] != 'RED']
    # # return order_company_salesperson[['name']]
    df = pd.merge(orders, company, on='com_id')
    red_ordrs = df[df['name'] == 'RED']
    invalid_ids = red_ordrs['sales_id'].unique()
    valid_sales_person = sales_person[~sales_person['sales_id'].isin(invalid_ids)]
    return valid_sales_person[['name']]