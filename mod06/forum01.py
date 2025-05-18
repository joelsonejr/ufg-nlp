import pandas as pd

df = pd.read_csv('./olist.csv')

stopwords_personalizadas = [
    'de', 'do', 'da', 'em', 'na', 'no', 'que', 'um', 'uma', 'foi',
    'com', 'para', 'eu', 'mas', 'muito', 'bom', 'ótimo', 'otimo',
    'produto', 'comprei', 'chegou', 'recebi'
]

# atualizando o df
df['review_preproc'] = df['review_preproc'].apply(
    lambda x:  ' '.join([termo for termo in x.split() if termo not in stopwords_personalizadas]))





