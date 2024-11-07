import pandas as pd 

df_meta = pd.read_csv('news-portal-user-interactions-by-globocom/articles_metadata.csv')

df_click = pd.read_csv('news-portal-user-interactions-by-globocom/clicks_sample.csv')

print(df_click.info())