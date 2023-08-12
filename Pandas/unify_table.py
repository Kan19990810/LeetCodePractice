import pandas as pd



if __name__ == '__main__':
    file1_path = r'C:\Users\83430\OneDrive\test.csv'
    file2_path = r'C:\Users\83430\OneDrive\econimy_level.csv'

    file1 = pd.read_csv(file1_path)
    file2 = pd.read_csv(file2_path)
    file1['SgnYear'] = file1['SgnYear'].astype(pd.StringDtype())
    file1['AreaName'] = file1['AreaName'].astype(pd.StringDtype())
    file2['city'] = file2['city'].astype(pd.StringDtype())

    file2['city'][file2.city == '上海'] = '上海市'
    file2['city'][file2.city == '云南'] = '云南省'
    file2['city'][file2.city == '内蒙古'] = '内蒙古自治区'
    file2['city'][file2.city == '北京'] = '北京市'
    file2['city'][file2.city == '吉林'] = '吉林省'
    file2['city'][file2.city == '四川'] = '四川省'
    file2['city'][file2.city == '河北'] = '河北省'
    file2['city'][file2.city == '天津'] = '天津市'
    file2['city'][file2.city == '宁夏'] = '宁夏回族自治区'
    file2['city'][file2.city == '安徽'] = '安徽省'
    file2['city'][file2.city == '河南'] = '河南省'
    file2['city'][file2.city == '山东'] = '山东省'
    file2['city'][file2.city == '山西'] = '山西省'
    file2['city'][file2.city == '广东'] = '广东省'
    file2['city'][file2.city == '广西'] = '广西壮族自治区'
    file2['city'][file2.city == '新疆'] = '新疆维吾尔自治区'
    file2['city'][file2.city == '江苏'] = '江苏省'
    file2['city'][file2.city == '江西'] = '江西省'
    file2['city'][file2.city == '浙江'] = '浙江省'
    file2['city'][file2.city == '海南'] = '海南省'
    file2['city'][file2.city == '湖北'] = '湖北省'
    file2['city'][file2.city == '湖南'] = '湖南省'
    file2['city'][file2.city == '甘肃'] = '甘肃省'
    file2['city'][file2.city == '福建'] = '福建省'
    file2['city'][file2.city == '西藏'] = '西藏自治区'
    file2['city'][file2.city == '贵州'] = '贵州省'
    file2['city'][file2.city == '辽宁'] = '辽宁省'
    file2['city'][file2.city == '重庆'] = '重庆市'
    file2['city'][file2.city == '陕西'] = '陕西省'
    file2['city'][file2.city == '青海'] = '青海省'
    file2['city'][file2.city == '黑龙江'] = '黑龙江省'
    # file2 = file2.groupby(['city']).nunique().reset_index()
    file1.rename(columns={'income': '营业收入/亿元'}, inplace=True)
    file2.rename(columns={'year': 'SgnYear', 'city': 'AreaName'}, inplace=True)

    file1['营业收入/亿元'] = file1['营业收入/亿元'].astype(pd.StringDtype())
    file2['SgnYear'] = file2['SgnYear'].astype(pd.StringDtype())
    file2['AreaName'] = file2['AreaName'].astype(pd.StringDtype())

    file1 = pd.merge(file1, file2, on=['SgnYear', 'AreaName'], how='left')

    # file1.to_csv('unify.csv', encoding='utf-8')

    file3_path = r'C:\Users\83430\OneDrive\population.csv'
    file3 = pd.read_csv(file3_path)
    file3['city'] = file3['city'].astype(pd.StringDtype())
    file3['city'][file3.city == '上海'] = '上海市'
    file3['city'][file3.city == '云南'] = '云南省'
    file3['city'][file3.city == '内蒙古'] = '内蒙古自治区'
    file3['city'][file3.city == '北京'] = '北京市'
    file3['city'][file3.city == '吉林'] = '吉林省'
    file3['city'][file3.city == '四川'] = '四川省'
    file3['city'][file3.city == '河北'] = '河北省'
    file3['city'][file3.city == '天津'] = '天津市'
    file3['city'][file3.city == '宁夏'] = '宁夏回族自治区'
    file3['city'][file3.city == '安徽'] = '安徽省'
    file3['city'][file3.city == '河南'] = '河南省'
    file3['city'][file3.city == '山东'] = '山东省'
    file3['city'][file3.city == '山西'] = '山西省'
    file3['city'][file3.city == '广东'] = '广东省'
    file3['city'][file3.city == '广西'] = '广西壮族自治区'
    file3['city'][file3.city == '新疆'] = '新疆维吾尔自治区'
    file3['city'][file3.city == '江苏'] = '江苏省'
    file3['city'][file3.city == '江西'] = '江西省'
    file3['city'][file3.city == '浙江'] = '浙江省'
    file3['city'][file3.city == '海南'] = '海南省'
    file3['city'][file3.city == '湖北'] = '湖北省'
    file3['city'][file3.city == '湖南'] = '湖南省'
    file3['city'][file3.city == '甘肃'] = '甘肃省'
    file3['city'][file3.city == '福建'] = '福建省'
    file3['city'][file3.city == '西藏'] = '西藏自治区'
    file3['city'][file3.city == '贵州'] = '贵州省'
    file3['city'][file3.city == '辽宁'] = '辽宁省'
    file3['city'][file3.city == '重庆'] = '重庆市'
    file3['city'][file3.city == '陕西'] = '陕西省'
    file3['city'][file3.city == '青海'] = '青海省'
    file3['city'][file3.city == '黑龙江'] = '黑龙江省'
    file3.rename(columns={'year': 'SgnYear', 'city': 'AreaName'}, inplace=True)
    file3['SgnYear'] = file3['SgnYear'].astype(pd.StringDtype())
    file3['AreaName'] = file3['AreaName'].astype(pd.StringDtype())
    file1 = pd.merge(file1, file3, on=['SgnYear', 'AreaName'], how='left')

    file4_path = r'C:\Users\83430\OneDrive\investment.csv'
    file4 = pd.read_csv(file4_path)
    file4['city'] = file4['city'].astype(pd.StringDtype())
    file4['city'][file4.city == '上海'] = '上海市'
    file4['city'][file4.city == '云南'] = '云南省'
    file4['city'][file4.city == '内蒙古'] = '内蒙古自治区'
    file4['city'][file4.city == '北京'] = '北京市'
    file4['city'][file4.city == '吉林'] = '吉林省'
    file4['city'][file4.city == '四川'] = '四川省'
    file4['city'][file4.city == '河北'] = '河北省'
    file4['city'][file4.city == '天津'] = '天津市'
    file4['city'][file4.city == '宁夏'] = '宁夏回族自治区'
    file4['city'][file4.city == '安徽'] = '安徽省'
    file4['city'][file4.city == '河南'] = '河南省'
    file4['city'][file4.city == '山东'] = '山东省'
    file4['city'][file4.city == '山西'] = '山西省'
    file4['city'][file4.city == '广东'] = '广东省'
    file4['city'][file4.city == '广西'] = '广西壮族自治区'
    file4['city'][file4.city == '新疆'] = '新疆维吾尔自治区'
    file4['city'][file4.city == '江苏'] = '江苏省'
    file4['city'][file4.city == '江西'] = '江西省'
    file4['city'][file4.city == '浙江'] = '浙江省'
    file4['city'][file4.city == '海南'] = '海南省'
    file4['city'][file4.city == '湖北'] = '湖北省'
    file4['city'][file4.city == '湖南'] = '湖南省'
    file4['city'][file4.city == '甘肃'] = '甘肃省'
    file4['city'][file4.city == '福建'] = '福建省'
    file4['city'][file4.city == '西藏'] = '西藏自治区'
    file4['city'][file4.city == '贵州'] = '贵州省'
    file4['city'][file4.city == '辽宁'] = '辽宁省'
    file4['city'][file4.city == '重庆'] = '重庆市'
    file4['city'][file4.city == '陕西'] = '陕西省'
    file4['city'][file4.city == '青海'] = '青海省'
    file4['city'][file4.city == '黑龙江'] = '黑龙江省'
    file4.rename(columns={'year': 'SgnYear', 'city': 'AreaName'}, inplace=True)
    file4['SgnYear'] = file4['SgnYear'].astype(pd.StringDtype())
    file4['AreaName'] = file4['AreaName'].astype(pd.StringDtype())
    file1 = pd.merge(file1, file4, on=['SgnYear', 'AreaName'], how='left')

    file5_path = r'C:\Users\83430\OneDrive\finance.csv'
    file5 = pd.read_csv(file5_path)
    file5.rename(columns={'时间': 'year', '地区': 'city'}, inplace=True)
    file5['city'] = file5['city'].astype(pd.StringDtype())
    file5['city'][file5.city == '上海'] = '上海市'
    file5['city'][file5.city == '云南'] = '云南省'
    file5['city'][file5.city == '内蒙古'] = '内蒙古自治区'
    file5['city'][file5.city == '北京'] = '北京市'
    file5['city'][file5.city == '吉林'] = '吉林省'
    file5['city'][file5.city == '四川'] = '四川省'
    file5['city'][file5.city == '河北'] = '河北省'
    file5['city'][file5.city == '天津'] = '天津市'
    file5['city'][file5.city == '宁夏'] = '宁夏回族自治区'
    file5['city'][file5.city == '安徽'] = '安徽省'
    file5['city'][file5.city == '河南'] = '河南省'
    file5['city'][file5.city == '山东'] = '山东省'
    file5['city'][file5.city == '山西'] = '山西省'
    file5['city'][file5.city == '广东'] = '广东省'
    file5['city'][file5.city == '广西'] = '广西壮族自治区'
    file5['city'][file5.city == '新疆'] = '新疆维吾尔自治区'
    file5['city'][file5.city == '江苏'] = '江苏省'
    file5['city'][file5.city == '江西'] = '江西省'
    file5['city'][file5.city == '浙江'] = '浙江省'
    file5['city'][file5.city == '海南'] = '海南省'
    file5['city'][file5.city == '湖北'] = '湖北省'
    file5['city'][file5.city == '湖南'] = '湖南省'
    file5['city'][file5.city == '甘肃'] = '甘肃省'
    file5['city'][file5.city == '福建'] = '福建省'
    file5['city'][file5.city == '西藏'] = '西藏自治区'
    file5['city'][file5.city == '贵州'] = '贵州省'
    file5['city'][file5.city == '辽宁'] = '辽宁省'
    file5['city'][file5.city == '重庆'] = '重庆市'
    file5['city'][file5.city == '陕西'] = '陕西省'
    file5['city'][file5.city == '青海'] = '青海省'
    file5['city'][file5.city == '黑龙江'] = '黑龙江省'
    file5.rename(columns={'year': 'SgnYear', 'city': 'AreaName'}, inplace=True)
    file5['SgnYear'] = file5['SgnYear'].astype(pd.StringDtype())
    file5['AreaName'] = file5['AreaName'].astype(pd.StringDtype())
    file1 = pd.merge(file1, file5, on=['SgnYear', 'AreaName'], how='left')
    file1 = file1.sort_values(by=['AreaName', 'SgnYear'])
    file1.to_csv('unify.csv', encoding='utf_8_sig')
    print(file1.head())