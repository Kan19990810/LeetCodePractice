import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # 分组查询 最小值的行 groupby min
    # groupby 需要重新设置索引
    df = activity.groupby('player_id')['event_date'].min().reset_index()

    return df.rename(columns={'event_data': 'first_login'})