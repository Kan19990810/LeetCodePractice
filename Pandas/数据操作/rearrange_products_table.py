import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # 重构表结构
    # 合并表格
    # notna() 布尔掩码 过滤包含空值的行 .notnull() 返回不为空的行
    # loc 选择过滤后行的列 .loc[行, [列]]
    # concat() 数据结构连接
    a = products.loc[products['store1'].notna(), ['product_id', 'store1']]
    a['store'] = 'store1'
    a.rename(columns={'store1': 'price'}, inplace=True)
    a = a[['product_id', 'store', 'price']]

    b = products.loc[products['store2'].notna(), ['product_id', 'store2']]
    b['store'] = 'store2'
    b.rename(columns={'store2': 'price'}, inplace=True)
    b = b[['product_id', 'store', 'price']]

    c = products.loc[products['store3'].notna(), ['product_id', 'store3']]
    c['store'] = 'store3'
    c.rename(columns={'store3': 'price'}, inplace=True)
    c = c[['product_id', 'store', 'price']]

    answer = pd.concat([a, b, c], axis=0)
    return answer