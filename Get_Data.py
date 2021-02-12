import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objs as go
import pandas as pd
import numpy as np


df = pd.read_csv("https://raw.githubusercontent.com/AbshkPskr/Zomato-Analysis/master/reviews.csv",
                 names = ['name','rating','date','cust_rating','review','sentiment']).drop_duplicates()

rest_names = df.groupby('name').count().sort_values('rating',ascending = False).head(20).index.to_list()
df = df[df.name.isin(rest_names)]
df['rating'] = df['rating'].astype('float')
df['date'] = pd.to_datetime(df['date'])
df['cust_rating'] = df['cust_rating'].astype('float')
df['review'] = df['review'].astype('string')
df['sentiment'] = df['sentiment'].astype('float').round(2)


import emoji
heart = emoji.emojize(':smile:',use_aliases=True)

stylecss = '''body {
    font-family: "Open Sans", sans-serif;
    background-color: red;
    margin: 0;
}'''

import os
if not os.path.exists('assets'):
    os.makedirs('assets')
sc = open("assets/style.css","w")
sc.write(stylecss)
sc.close()