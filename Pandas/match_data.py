import pandas as pd

if __name__ == '__main__':
    file1_path = r'C:\Users\Kan\Desktop\unify_1.csv'
    file2_path = r'C:\Users\Kan\Desktop\RD.csv'
    
    file1 = pd.read_csv(file1_path)
    file2 = pd.read_csv(file2_path)
    # topic1 = ['SgnYear', 'AreaName', 'InternetUsers', 'BroadBandSub']
    topic2 = ['SgnYear', 'AreaName', 'RDProjectExpenditure']
    df1 = file1
    df2 = file2[topic2].iloc[2:]
    # # df1['SgnYear'] = df1['SgnYear'].astype(object)
    # df1['AreaName'] = df1['AreaName'].astype(object)
    # # df2['SgnYear'] = df2['SgnYear'].astype(object)
    # df2['AreaName'] = df2['AreaName'].astype(object)
    df1['SgnYear'] = df1['SgnYear'].astype(pd.StringDtype())
    df1['AreaName'] = df1['AreaName'].astype(pd.StringDtype())
    df2['SgnYear'] = df2['SgnYear'].astype(pd.StringDtype())
    df2['AreaName'] = df2['AreaName'].astype(pd.StringDtype())
    # df2['income'] = df2['income'].astype('float64')
    # df2['Operating revenue/100 million'] = df2['Operating revenue/100 million'].astype(object)s
    # file1 = file1.set_axis(file1.iloc[0], axis=1, inplace=False)
    new_file = pd.merge(df1, df2, on = ['SgnYear','AreaName'],  how = 'left')

    # file3_path = r'C:\Users\Kan\OneDrive\research.csv'
    # file3 = pd.read_csv(file3_path)
    # topic3 = ['SgnYear', 'AreaName', 'RDinstitutions', 'RDProject', 'PatentApplicationPatent']
    # df3 = file3[topic3].iloc[2:]
    # df3['SgnYear'] = df3['SgnYear'].astype(pd.StringDtype())
    # df3['AreaName'] = df3['AreaName'].astype(pd.StringDtype())
    # new_file = pd.merge(new_file, df3, on = ['SgnYear','AreaName'],  how = 'left')


    # file4_path = r'C:\Users\Kan\OneDrive\application.csv'
    # file4 = pd.read_csv(file4_path)
    # topic4 = ['SgnYear', 'AreaName', 'NewProductSalesRevenue']
    # df4 = file4[topic4].iloc[2:]
    # df4['SgnYear'] = df4['SgnYear'].astype(pd.StringDtype())
    # df4['AreaName'] = df4['AreaName'].astype(pd.StringDtype())
    # new_file = pd.merge(new_file, df4, on = ['SgnYear','AreaName'],  how = 'left')

    new_file.to_csv('unify_2.csv',encoding='utf-8-sig')
    # print(df1.head())
    # print(df2.head())
    print(new_file.head())
    # print(new_file['营业收入/亿元'].describe())