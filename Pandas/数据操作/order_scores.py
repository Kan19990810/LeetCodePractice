import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # 排序 rank() 计算沿轴对的数值数据排名 method='dense'密集排名
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores[['score', 'rank']].sort_values('score', ascending=False)