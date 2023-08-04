import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # groupby + size 分组筛查大小 .reset_index: 给size 列命名
    df = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='counts')
    df = df[df['counts'] >= 3][['actor_id', 'director_id']]
    return df